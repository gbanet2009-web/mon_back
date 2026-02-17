from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,   # login → obtient access + refresh
    TokenRefreshView       # refresh token
)
from . import views  # tes vues api existantes

urlpatterns = [
    # JWT Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Tes endpoints API
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('exercises/', views.ExerciseListView.as_view(), name='exercises'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]