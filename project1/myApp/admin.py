from django.contrib import admin

# Register your models here.
# 모델파일 임프트
# Student, City 테이블
from .models import Student, City

# Register your models here.
# 관리자 페이지에 모델 추가
admin.site.register(Student)
admin.site.register(City)