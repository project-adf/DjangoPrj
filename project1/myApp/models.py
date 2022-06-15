from django.db import models

# Create your models here.
# ORM 방식으로 테이블 생성
# 학생 테이블
class Student(models.Model):
    s_name = models.CharField(max_length=100)  # 학생명
    s_major = models.CharField(max_length=100)  # 전공
    s_age = models.IntegerField(default=0) # 나이
    s_grade = models.IntegerField(default=0) # 점수
    s_gender = models.CharField(max_length=30) # 성별

    def __str__(self):
        return self.s_name

# City 테이블 모델 정의
class City(models.Model):
    name = models.CharField(max_length=100)   # 도시명
    population = models.IntegerField(default=0)  # 인구수

    def __str__(self):
        return self.name