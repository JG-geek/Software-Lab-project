from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from LoginRegister.models import courseData
import plotly.graph_objects as go
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login/')
def yearWiseComparison(request):
    if(request.method == "POST"):
        course_code = request.POST['course_code']
        semester = request.POST['semester']
        courseData_objects = courseData.objects.filter(course_code=course_code, sem=semester)
        if(courseData_objects.count() == 0):
            messages.info(request, 'No data found for the given course code and semester')
            return redirect('/plots/yearWiseComparison/')
        else:    
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('total', flat=True)), mode='lines+markers'))                    
            fig.update_layout(title_text='Total Students vs Year', xaxis_title='Year', yaxis_title='Total Students')
            fig = fig.to_html(full_html=False, default_height=500, default_width=700)
            return render(request, 'yearWiseComparison.html', context={'plot_div': fig})

    else:
        courseData_objects = courseData.objects.values_list('course_code', flat=True).distinct().order_by('course_code')
        return render(request, 'yearWiseComparison.html', context={'courseData_objects': courseData_objects})