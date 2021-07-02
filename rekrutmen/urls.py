from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/',views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('hdc/', views.hdc, name='hdc'),
    path('hdc/job/', views.add_job, name='add_job'),
    path('hdc/job/edit/<int:id>/', views.edit_job, name='edit_job'),
    path('hdc/job/<int:id>/', views.detail_job, name='detail_job'),
    path('hdc/job/<int:id>/pelamar/<int:id2>', views.detail_pelamar, name='detail_pelamar'),

    path('pelamar/lamar/<int:id>/', views.lamar, name='lamar'),
    path('pelamar/', views.pelamar, name='pelamar'),
    path('pelamar/test/<int:id>/', views.do_the_tests, name='test'),
]