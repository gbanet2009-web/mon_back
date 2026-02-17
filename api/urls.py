from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('update-class/', views.UpdateClassView.as_view(), name='update_class'),
    path('add-credits/', views.AddCreditsView.as_view(), name='add_credits'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('exercises/', views.ExerciseListView.as_view(), name='exercises'),
    path('bac-subjects/', views.BacSubjectListView.as_view(), name='bac_subjects'),
]