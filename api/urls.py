from django.urls import path
from .views import CourseListView, ExerciseListView, UserProfileView, LoginView, UpdateClassView, AddCreditsView, BacSubjectListView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='courses'),
    path('exercises/', ExerciseListView.as_view(), name='exercises'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('update_class/', UpdateClassView.as_view(), name='update_class'),
    path('add_credits/', AddCreditsView.as_view(), name='add_credits'),
    path('bac_subjects/', BacSubjectListView.as_view(), name='bac_subjects'),
]
