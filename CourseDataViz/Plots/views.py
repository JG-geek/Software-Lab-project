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
            line = go.Figure()
            line.add_trace(go.Scatter(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('total', flat=True)), mode='lines+markers', name="Total Students"))                    
            line.update_layout(title_text='Total Students vs Year', xaxis_title='Year', yaxis_title='Total Students')
            line = line.to_html(full_html=False, default_height=500, default_width=700)

            bar = go.Figure()
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_AA', flat=True)), name="Grade AA"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_AB', flat=True)), name="Grade AB"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_BB', flat=True)), name="Grade BB"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_BC', flat=True)), name="Grade BC"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_CC', flat=True)), name="Grade CC"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_CD', flat=True)), name="Grade CD"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_DD', flat=True)), name="Grade DD"))
            bar.update_layout(title_text='Grade vs Year', xaxis_title='Year', yaxis_title='Grade')
            bar = bar.to_html(full_html=False, default_height=500, default_width=700)

            return render(request, 'yearWiseComparison.html', context={'line': line, 'bar': bar})

    else:
        courseData_objects = courseData.objects.values_list('course_code', flat=True).distinct().order_by('course_code')
        return render(request, 'yearWiseComparison.html', context={'courseData_objects': courseData_objects})