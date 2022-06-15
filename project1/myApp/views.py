# redirect 소스 추가
from django.shortcuts import render, redirect
from django.http import HttpResponse
# 추가
import csv
import os
# 추가
import pandas as pd
import numpy as np
# 추가
import json
import requests
# 추가 데이타베이스 연동
# Sutudent, City 테이블 연결
from .models import Student, City

# 데이타프레임의 컬럼을 10컬럼까지 모두 표시
pd.set_option('display.max_columns', 10)

# Create your views here.

# /, /myApp/ 주소와 연결되는 뷰함수
def index(request):
    return render(request, 'myApp/main_test1.html')


# /myApp/sub1 주소와 연결되는 뷰함수
def sub1(request):
    return render(request, 'myApp/sub1.html')

# /myApp/sub2 주소와 연결되는 뷰함수
def sub2(request):
    return render(request, 'myApp/sub2.html')

# /myApp/sub3 주소와 연결되는 뷰함수
def sub3(request):
    # 딕셔너리 형태로 전송 데이타 정의
    context = {
                'name':'임영웅',
                'id':'YYY',
                'age':34,
                'grade':[ 90, 85, 77]

    }
    return render(request, 'myApp/sub3.html', context)


# /myApp/sub4 주소와 연결되는 뷰함수
def sub4(request):

    # 리스트안에 튜플로 정의 => 튜플리스트 2차원
    # 4행 2열 스타일
    book_info = [
        ('title', '어린왕자'),
        ('writer', '생텍쥐페리'),
        ('price', 15000),
        ('ISBN', '483731-849-90'),
    ]

    # 5행 4열 스타일
    student_info = [
        ('홍길동', '남', '부산', 23),
        ('고길동', '남', '전주', 28),
        ('윤길동', '남', '서울', 23),
        ('박길동', '남', '마산', 23),
        ('정길순', '여', '울산', 22),
    ]

    # 딕셔너리 형태로 전송 데이타 정의
    context = {
           'book_info':  book_info,
           'student_info' :  student_info,
           'numList' : range(1,101,2), # [1, 3, ... 99]
    }

    return render(request, 'myApp/sub4.html', context)


# /myApp/sub5 주소와 연결되는 뷰함수
def sub5(request):

    # 리스트안에 튜플로 정의 => 튜플리스트 2차원
    # 4행 2열 스타일
    book_list = [
        ('파이썬 도장', 33000),
        ('C언어', 23000),
        ('JAVA', 43000),
    ]

    context = {
                'book_list' : book_list ,
                }
    return render(request, 'myApp/sub5.html', context)


# /myApp/sub6 주소와 연결되는 뷰함수
def sub6(request):
    # 현재 경로 위치 확인
    print('현재위치는?', os.getcwd())

    # data.csv => csv 객체 => 리스트 => context
    with open('myApp/data/data.csv', 'r') as f:
        csv_data = csv.reader(f)

        data_list = []
        for row in csv_data:
            data_list.append(row)
            print(row)

    context = {
                'data_list' : data_list
                }
    return render(request, 'myApp/sub6.html', context)


# /myApp/sub7 주소와 연결되는 뷰함수
def sub7(request):

    # csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/bestbook10.csv', encoding='cp949')
    arr = df.to_numpy()
    data_list = arr.tolist()

    context = {
                'data_list' : data_list
                }
    return render(request, 'myApp/sub7.html', context)

# /myApp/sub8 주소와 연결되는 뷰함수
def sub8(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/1480523/MetalMeasuringResultService/MetalService'
    service_key = 'Yhq6n9vlpaKZsCOw0jec8zIdZ8p+Bpuku6WLjVgDhqXRW6dHnfXoauSEj19jpnjv59CUGspyTxVCgCeXOua7dg=='
    params = {'serviceKey': service_key,
              'pageNo': '1',
              'numOfRows': '12',
              'resultType': 'JSON',
              'date': '20220609',
              'stationcode': '3',
              'itemcode': '90303',
              'timecode': 'RH02'}

    response = requests.get(url, params=params)

    dust = json.loads(response.text)

    df_dust = pd.DataFrame(dust['MetalService']['item'],
                           columns=['SDATE', 'STATIONCODE', 'ITEMCODE', 'TIMECODE', 'VALUE'])
    print(df_dust)

    arr = df_dust.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/sub8.html', context)

# /myApp/sub9 주소와 연결되는 뷰함수
def sub9(request):
    return render(request, 'myApp/sub9.html')

# /myApp/sub10 주소와 연결되는 뷰함수
def sub10(request):
    return render(request, 'myApp/sub10.html')

# /myApp/sub11 주소와 연결되는 뷰함수
def sub11(request):
    return render(request, 'myApp/sub11.html')

# /myApp/sub12/ 주소와 연결되는 뷰함수
def sub12(request):
    return render(request, 'myApp/sub12.html')

# /myApp/numberCon/ 주소와 연결되는 뷰함수
# 짝수인지 홀수인지 메세지 출력
def numberCon(request):
    # 폼에서 GET 방식으로 전달받은 데이타를 변수에 저장
    # 'number'는 html 페이지의 form의 텍스트필드의 name 값
    number = request.GET['number']
    try:
        # 입력된 숫자(문자 형태 등)를 정수형으로 변경
        number = int(number)
    except:
        # 에러 발생시 메세지
        result = "숫자가 아니에요"
    else:
        # 정수로 변경된다면
        if number%2 == 0:
            result = '짝수'
        else:
            result = '홀수'

    # 결과 페이지에 전송할 데이타를 딕셔너리로 저장
    context = {
            'number' : number, # 입력값
            'result' : result, # 결과 메세지
            }
    # return HttpResponse(result)
    return render(request, 'myApp/sub12_result.html', context)

# POST 방식의 입력 페이지
# /myApp/sub13/ 주소와 연결되는 뷰함수
def sub13(request):
    return render(request, 'myApp/sub13.html')

# POST 방식의 결과 페이지
# /myApp/messageCon 주소와 연결되는 뷰함수
def messageCon(request):
    # POST 방식으로 전달받은 데이타를 변수에 저장
    userName = request.POST['userName']
    result = f'{userName} 님... 오늘도 편안한 하루 되세요...'
    context = {
        'result':result,
    }
    return render(request, 'myApp/sub13_result.html', context)

# 테이블 전체
# /myApp/all/ 주소와 연결되는 뷰함수
def all(request):
    # Student 모델의 모든 레코드를 저장
    # select * from myApp_student; 결과를 저장
    # 테이블명.objects.all()
    student_list =  Student.objects.all()
    # 딕셔너리로 선언
    context = {'student_list':student_list}
    return render(request, 'myApp/all.html', context)

# /myApp/학생아이디/detail/ 주소와 연결되는 뷰함수
# 학생 한명에 대한 상세
def detail(request, id):
    # select * from myApp_student where id=학생아이디;
    # 변수 = Student.objects.get(필드명=값)
    # id 값에 해당하는 학생 한명 정보
    student = Student.objects.get(id=id)
    context = {'student': student}
    return render(request, 'myApp/detail.html', context)

# 학생 추가 페이지
# /myApp/register/ 주소와 연결되는 뷰함수
def register(request):
    return render(request, 'myApp/register.html')

# /myApp/registerCon/ 주소와 연결되는 뷰함수
# 학생 추가 DB 반영
def registerCon(request):
    # 데이타 전달
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    # DB 반영
    # 인스턴스변수 = 클래스명(필드=값....)
    # 인스턴스변수.save()
    student = Student(s_name=name, s_major=major, s_age=age, s_grade=grade, s_gender=gender)
    student.save()

    # return HttpResponse("추가 완료")
    # 학생 전체보기 페이지로 이동
    return redirect('/myApp/all/')

# 학생 삭제
def delete(request, id):
    # 변수 = Student.objects.get(필드명=값)
    student = Student.objects.get(id=id)
    # 테이블에서 해당 아이디에 해당하는 레코드를 삭제 반영
    student.delete()

    # 학생 전체보기 페이지로 이동
    return redirect('/myApp/all/')


def modify(request, id):
    # id 에 해당하는 학생 레코드를 저장
    # 변수명 = Student.objects.get(필드명=값)
    student = Student.objects.get(id=id)
    # 딕셔너리 형태로 전달
    context = {'student': student}
    return render(request, 'myApp/modify.html', context)


# 학생 수정 DB 반영
def modifyCon(request):
    # 데이타 전달
    id = request.POST['id']
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    # 학생 레코드 찾기
    student = Student.objects.get(id=id)

    # 데이타 수정
    student.s_name = name
    student.s_major = major
    student.s_age = age
    student.s_grade = grade
    student.s_gender = gender

    # DB 테이블에 반영
    student.save()

    # 학생 상세페이지로 이동
    # /myApp/학생아이디/detail/
    return redirect(f'/myApp/{id}/detail')

# /myApp/city 주소와 연결되는 뷰함수
# City 테이블 모델에서 전체 레코드를 저장하고
# 관련 html 문서에 전달
def city(request):
    # 테이블모델명.objects.all()
    city_list = City.objects.all()
    # 딕셔너리 구조로 만들어서 html 문서에 전달
    context = {'city_list':city_list}
    return render(request, 'myApp/city.html', context)

# /myApp/search/ 주소와 연결되는 뷰함수
def search(request):
    return render(request, 'myApp/search.html')


# /myApp/searchCon/ 주소와 연결되는 뷰함수
def searchCon(request):
    # 폼에서 GET방식으로 전달받은 데이타를 변수에 저장
    search_word = request.GET['search']
    # 결과리스트명 = 테이블명.objects.filter(필드명_icontains=search_word)
    city_list = City.objects.filter(name__icontains=search_word)
    print('=' * 50)
    print(search_word, city)

    # 딕셔너리 구조로 만들어서 html 문서에 전달
    context = {'city_list': city_list}

    return render(request, 'myApp/search_result.html', context)



# /myApp/miniPrj1 주소와 연결되는 뷰함수
def miniPrj1_1(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '북구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_1.html', context)


# /myApp/miniPrj1_2 주소와 연결되는 뷰함수
def miniPrj1_2(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '중구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_2.html', context)



# /myApp/miniPrj1_3 주소와 연결되는 뷰함수
def miniPrj1_3(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '서구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_3.html', context)



# /myApp/miniPrj1_4 주소와 연결되는 뷰함수
def miniPrj1_4(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '동구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_4.html', context)



# /myApp/miniPrj1_5 주소와 연결되는 뷰함수
def miniPrj1_5(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '영도구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_5.html', context)



# /myApp/miniPrj1_6 주소와 연결되는 뷰함수
def miniPrj1_6(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '부산진구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_6.html', context)



# /myApp/miniPrj1_7 주소와 연결되는 뷰함수
def miniPrj1_7(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '동래구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_7.html', context)



# /myApp/miniPrj1_8 주소와 연결되는 뷰함수
def miniPrj1_8(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '남구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_8.html', context)



# /myApp/miniPrj1_9 주소와 연결되는 뷰함수
def miniPrj1_9(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '해운대구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_9.html', context)



# /myApp/miniPrj1_10 주소와 연결되는 뷰함수
def miniPrj1_10(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '사하구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_10.html', context)



# /myApp/miniPrj1_11 주소와 연결되는 뷰함수
def miniPrj1_11(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '금정구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_11.html', context)



# /myApp/miniPrj1_12 주소와 연결되는 뷰함수
def miniPrj1_12(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '강서구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_12.html', context)



# /myApp/miniPrj1_13 주소와 연결되는 뷰함수
def miniPrj1_13(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '연제구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_13.html', context)



# /myApp/miniPrj1_14 주소와 연결되는 뷰함수
def miniPrj1_14(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '수영구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_14.html', context)



# /myApp/miniPrj1_15 주소와 연결되는 뷰함수
def miniPrj1_15(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '사상구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_15.html', context)



# /myApp/miniPrj1_16 주소와 연결되는 뷰함수
def miniPrj1_16(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanLifeInfoService/getLifeInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params ={'serviceKey' : serviceKey,
             'pageNo' : '1',
             'numOfRows' : '2000',
             'resultType' : 'json' }

    response = requests.get(url, params=params)

    lifeinfo = json.loads(response.text)

    df_lifeinfo_list = pd.DataFrame(lifeinfo['getLifeInfo']['item'],
                           columns=['examinDe','pumNm','gugunNm','itemName','unit','unitprice','rm','bsshNm','adres','la','lo'])
    print(df_lifeinfo_list)

    GU = df_lifeinfo_list[df_lifeinfo_list['gugunNm'] == '기장군']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj1_16.html', context)


# /myApp/miniPrj2_1 주소와 연결되는 뷰함수
def miniPrj2_1(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '북구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_1.html', context)



# /myApp/miniPrj2_2 주소와 연결되는 뷰함수
def miniPrj2_2(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '중구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_2.html', context)


# /myApp/miniPrj2_3 주소와 연결되는 뷰함수
def miniPrj2_3(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '서구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_3.html', context)


# /myApp/miniPrj2_4 주소와 연결되는 뷰함수
def miniPrj2_4(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '동구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_4.html', context)


# /myApp/miniPrj2_5 주소와 연결되는 뷰함수
def miniPrj2_5(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '영도구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_5.html', context)


# /myApp/miniPrj2_6 주소와 연결되는 뷰함수
def miniPrj2_6(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '부산진구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_6.html', context)


# /myApp/miniPrj2_7 주소와 연결되는 뷰함수
def miniPrj2_7(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '동래구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_7.html', context)


# /myApp/miniPrj2_8 주소와 연결되는 뷰함수
def miniPrj2_8(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '남구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_8.html', context)


# /myApp/miniPrj2_9 주소와 연결되는 뷰함수
def miniPrj2_9(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '해운대구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_9.html', context)


# /myApp/miniPrj2_10 주소와 연결되는 뷰함수
def miniPrj2_10(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '사하구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_10.html', context)


# /myApp/miniPrj2_11 주소와 연결되는 뷰함수
def miniPrj2_11(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '금정구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_11.html', context)


# /myApp/miniPrj2_12 주소와 연결되는 뷰함수
def miniPrj2_12(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '강서구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_12.html', context)


# /myApp/miniPrj2_13 주소와 연결되는 뷰함수
def miniPrj2_13(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '연제구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_13.html', context)


# /myApp/miniPrj2_14 주소와 연결되는 뷰함수
def miniPrj2_14(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '수영구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_14.html', context)


# /myApp/miniPrj2_15 주소와 연결되는 뷰함수
def miniPrj2_15(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '사상구']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_15.html', context)


# /myApp/miniPrj2_16 주소와 연결되는 뷰함수
def miniPrj2_16(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/BusanPrsnlSrvcInfoService/getPrsnlSrvcInfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '2000',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    psnsvc = json.loads(response.text)

    df_psnsvc_list = pd.DataFrame(psnsvc['getPrsnlSrvcInfo']['item'])

    print(df_psnsvc_list)

    GU = df_psnsvc_list[df_psnsvc_list['gugunNm'] == '기장군']

    arr = GU.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj2_16.html', context)


# /myApp/miniPrj3 주소와 연결되는 뷰함수
def miniPrj3(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/ByMarketCostTrend/getByMarketCostTrendinfo'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '300',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    ByMarketCostTrend = json.loads(response.text)

    ByMarketCostTrend_list = pd.DataFrame(ByMarketCostTrend['getByMarketCostTrendinfo']['item'])

    print(ByMarketCostTrend_list)

    arr = ByMarketCostTrend_list.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj3.html', context)


# /myApp/miniPrj3 주소와 연결되는 뷰함수
def miniPrj4(request):
    # openAPI => json 텍스트 => 리스트딕셔너리 => 컨텍스트 => 웹페이지
    url = 'http://apis.data.go.kr/6260000/EgMarketCost/getDailyCost'
    serviceKey = 'rysD8XENRiMMY3uk79ked4KvsaZOLjrN+A0MqNt5kj2y8qTJiDDHzbPQbngj3ztYx2VSZ1oFkAX9N4VQB+1ZSw=='
    params = {'serviceKey': serviceKey,
              'pageNo': '1',
              'numOfRows': '300',
              'resultType': 'json'}

    response = requests.get(url, params=params)

    EgMarketCost = json.loads(response.text)

    EgMarketCost_list = pd.DataFrame(EgMarketCost['getDailyCost']['item'])

    print(EgMarketCost_list)

    arr = EgMarketCost_list.to_numpy()
    data_list = arr.tolist()

    context = { 'data_list': data_list }

    return render(request, 'myApp/miniPrj4.html', context)


def store_page(request):
    url = 'http://apis.data.go.kr/6260000/GoodPriceStoreService/getGoodPriceStore'
    service_key = 'ux4SlBKiiFKYpgpQQ1ep0yaCKm7b7Vi4M23owm8bsRkAb6qLCIL6U25YlB8jQ91MPMaDgAyDfrh1iLR0eXjl7w=='
    params = {'serviceKey': service_key,
              'pageNo': '1',
              'numOfRows': '638',
              'resultType': 'json'
              }

    response = requests.get(url, params=params)

    # 2) json 으로 변경
    store = json.loads(response.content)

    # 3) 리스트 딕셔너리 => 데이타프레임
    df_store = pd.DataFrame(store['getGoodPriceStore']['item'],
                            columns=['parkngAt', 'bsnTime', 'creatDt', 'imgFile1', 'imgName1', 'imgFile2', 'imgName2',
                                     'sj', 'mNm', 'adres', 'tel', 'cn', 'locale', 'intrcn'])

    name = df_store.sj
    park = df_store.parkngAt
    time = df_store.bsnTime
    img1 = df_store.imgFile1
    img_name1 = df_store.imgName1
    img2 = df_store.imgFile2
    img_name2 = df_store.imgName2
    mNm = df_store.mNm
    addr = df_store.adres
    tel = df_store.tel
    cn = df_store.cn
    locale = df_store.locale
    intrcn = df_store.intrcn

    data_list = []
    for i in range(630):
        data_list.append((name[i], park[i], time[i], img1[i], img_name1[i], img2[i], img_name2[i], mNm[i], addr[i][7:-1],
                          tel[i], cn[i], locale[i], intrcn[i]))

    context = {
        'data_list': data_list,
    }

    return render(request, 'myApp/store_page.html', context)


def store_page2(request):
    url = 'http://apis.data.go.kr/6260000/GoodPriceStoreService/getGoodPriceStore'
    service_key = 'ux4SlBKiiFKYpgpQQ1ep0yaCKm7b7Vi4M23owm8bsRkAb6qLCIL6U25YlB8jQ91MPMaDgAyDfrh1iLR0eXjl7w=='
    params = {'serviceKey': service_key,
              'pageNo': '1',
              'numOfRows': '638',
              'resultType': 'json'
              }

    response = requests.get(url, params=params)

    # 2) json 으로 변경
    store = json.loads(response.content)

    # 3) 리스트 딕셔너리 => 데이타프레임
    df_store = pd.DataFrame(store['getGoodPriceStore']['item'],
                            columns=['parkngAt', 'bsnTime', 'creatDt', 'imgFile1', 'imgName1', 'imgFile2', 'imgName2',
                                     'sj', 'mNm', 'adres', 'tel', 'cn', 'locale', 'intrcn'])

    name = df_store.sj
    park = df_store.parkngAt
    time = df_store.bsnTime
    img1 = df_store.imgFile1
    img_name1 = df_store.imgName1
    img2 = df_store.imgFile2
    img_name2 = df_store.imgName2
    mNm = df_store.mNm
    addr = df_store.adres
    tel = df_store.tel
    cn = df_store.cn
    locale = df_store.locale
    intrcn = df_store.intrcn

    data_list = []
    for i in range(630):
        data_list.append((name[i], park[i], time[i], img1[i], img_name1[i], img2[i], img_name2[i], mNm[i], addr[i][7:-1],
                          tel[i], cn[i], locale[i], intrcn[i]))

    context = {
        'data_list': data_list,
    }

    return render(request, 'myApp/store_page2.html', context)