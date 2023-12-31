from django.db import models

# Create your models here.
class courseData(models.Model):
    course_code = models.TextField()
    year = models.TextField()
    sem = models.IntegerField()
    grade_AA = models.IntegerField()
    grade_AP = models.IntegerField()
    grade_AB = models.IntegerField()
    grade_BB = models.IntegerField()
    grade_BC = models.IntegerField()
    grade_CC = models.IntegerField()
    grade_CD = models.IntegerField()
    grade_DD = models.IntegerField()
    grade_AU = models.IntegerField()
    grade_DX = models.IntegerField()
    grade_FF = models.IntegerField()
    grade_FR = models.IntegerField()
    grade_II = models.IntegerField()
    grade_NP = models.IntegerField()
    grade_PP = models.IntegerField()
    grade_S = models.IntegerField()
    grade_XX = models.IntegerField()
    total = models.IntegerField()