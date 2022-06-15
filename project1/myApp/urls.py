# myApp\urls.py

from django.urls import path
from . import views

# 시작페이지 주소와 뷰함수 연결
urlpatterns = [

    # 시작페이지 주소와 뷰함수 연결
    path('', views.index),


    # /myApp/sub1/
    path('sub1/', views.sub1),

    # /myApp/sub2/
    path('sub2/', views.sub2),

    # /myApp/sub3/
    path('sub3/', views.sub3),

    # /myApp/sub4/
    path('sub4/', views.sub4),

    # /myApp/sub5/
    path('sub5/', views.sub5),

    # /myApp/sub6/
    path('sub6/', views.sub6),

    # /myApp/sub7/
    path('sub7/', views.sub7),

    # /myApp/sub8/
    path('sub8/', views.sub8),

    # /myApp/sub9/
    path('sub9/', views.sub9),

    # /myApp/sub10/
    path('sub10/', views.sub10),

    # /myApp/sub11/
    path('sub11/', views.sub11),

    # GET 테스트 URL
    # /myApp/sub12/
    path('sub12/', views.sub12),

    # form 태그에서 전송 버튼 클릭시 이동할 주소 URL
    # /myApp/numberCon/
    path('numberCon/', views.numberCon),

    # POST 테스트 URL
    # /myApp/sub13/
    path('sub13/', views.sub13),

    # POST 방식에서 form 태그에서 전송 버튼 클릭시 이동할 주소 URL
    # /myApp/messageCon/
    path('messageCon/', views.messageCon),

    # 학생목록 전체 보기
    # /myApp/all/
    path('all/', views.all),

    # 학생상세 주소
    # /myApp/학생아이디/detail/
    path('<id>/detail/', views.detail),

    # 학생 추가
    # /myApp/register/
    path('register/', views.register),

    # 학생 추가 DB 반영
    # /myApp/registerCon/
    path('registerCon/', views.registerCon),

    # 학생삭제 주소
    # /myApp/학생아이디/delete/
    path('<id>/delete/', views.delete),

    # 학생수정 주소
    # /myApp/학생아이디/modify/
    path('<id>/modify/', views.modify),

    # 학생 수정 DB 반영
    # /myApp/modifyCon/
    path('modifyCon/', views.modifyCon),

    # city 테이블 모델의 전체 목록 표시 주소
    # /myApp/city/
    path('city/', views.city),

    # 검색 입력폼 주소
    # /myApp/search/
    path('search/', views.search),

    # 검색 결과 주소
    # /myApp/searchCon/
    path('searchCon/', views.searchCon),

    # /myApp/miniPrj1_1/
    path('miniPrj1_1/', views.miniPrj1_1),

    # /myApp/miniPrj1_2/
    path('miniPrj1_2/', views.miniPrj1_2),

    # /myApp/miniPrj1_3/
    path('miniPrj1_3/', views.miniPrj1_3),

    # /myApp/miniPrj1_4/
    path('miniPrj1_4/', views.miniPrj1_4),

    # /myApp/miniPrj1_5/
    path('miniPrj1_5/', views.miniPrj1_5),

    # /myApp/miniPrj1_6/
    path('miniPrj1_6/', views.miniPrj1_6),

    # /myApp/miniPrj1_7/
    path('miniPrj1_7/', views.miniPrj1_7),

    # /myApp/miniPrj1_8/
    path('miniPrj1_8/', views.miniPrj1_8),

    # /myApp/miniPrj1_9/
    path('miniPrj1_9/', views.miniPrj1_9),

    # /myApp/miniPrj1_10/
    path('miniPrj1_10/', views.miniPrj1_10),

    # /myApp/miniPrj1_11/
    path('miniPrj1_11/', views.miniPrj1_11),

    # /myApp/miniPrj1_12/
    path('miniPrj1_12/', views.miniPrj1_12),

    # /myApp/miniPrj1_13/
    path('miniPrj1_13/', views.miniPrj1_13),

    # /myApp/miniPrj1_14/
    path('miniPrj1_14/', views.miniPrj1_14),

    # /myApp/miniPrj1_15/
    path('miniPrj1_15/', views.miniPrj1_15),

    # /myApp/miniPrj1_16/
    path('miniPrj1_16/', views.miniPrj1_16),

    # /myApp/miniPrj2_1/
    path('miniPrj2_1/', views.miniPrj2_1),

    # /myApp/miniPrj2_2/
    path('miniPrj2_2/', views.miniPrj2_2),

    # /myApp/miniPrj2_3/
    path('miniPrj2_3/', views.miniPrj2_3),

    # /myApp/miniPrj2_4/
    path('miniPrj2_4/', views.miniPrj2_4),

    # /myApp/miniPrj2_5/
    path('miniPrj2_5/', views.miniPrj2_5),

    # /myApp/miniPrj2_6/
    path('miniPrj2_6/', views.miniPrj2_6),

    # /myApp/miniPrj2_7/
    path('miniPrj2_7/', views.miniPrj2_7),

    # /myApp/miniPrj2_8/
    path('miniPrj2_8/', views.miniPrj2_8),

    # /myApp/miniPrj2_9/
    path('miniPrj2_9/', views.miniPrj2_9),

    # /myApp/miniPrj2_10/
    path('miniPrj2_10/', views.miniPrj2_10),

    # /myApp/miniPrj2_11/
    path('miniPrj2_11/', views.miniPrj2_11),

    # /myApp/miniPrj2_12/
    path('miniPrj2_12/', views.miniPrj2_12),

    # /myApp/miniPrj2_13/
    path('miniPrj2_13/', views.miniPrj2_13),

    # /myApp/miniPrj2_14/
    path('miniPrj2_14/', views.miniPrj2_14),

    # /myApp/miniPrj2_15/
    path('miniPrj2_15/', views.miniPrj2_15),

    # /myApp/miniPrj2_16/
    path('miniPrj2_16/', views.miniPrj2_16),

    # /myApp/miniPrj3/
    path('miniPrj3/', views.miniPrj3),

    # /myApp/miniPrj4/
    path('miniPrj4/', views.miniPrj4),

    # /myApp/store_page/
    path('store_page/', views.store_page),

    # /myApp/store_page/
    path('store_page2/', views.store_page2),
]