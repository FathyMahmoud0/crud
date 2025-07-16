from django.urls import path
from . import views

urlpatterns = [
    path ('',views.StudentList.as_view(),name = 'student_list'),
    path ('create/',views.StudentCreate.as_view(),name = 'student_create'),
    path ('update/<int:pk>/',views.StudentUpdate.as_view(),name = 'student_update'),
    path ('delete/<int:pk>/',views.StudentDelete.as_view(),name = 'student_delete'),
]
