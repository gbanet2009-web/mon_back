from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import CourseListView, ExerciseListView, ProfileView

urlpatterns = [
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API
    path('courses/', CourseListView.as_view(), name='courses'),
    path('exercises/', ExerciseListView.as_view(), name='exercises'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
