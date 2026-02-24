from django.urls import path
from .views import (
    DocumentListCreateView, 
    DocumentDetailView,
    RegisterView,
    LoginView,
    UserProfileView,
    AddCreditsView,
    PurchaseDocumentView,
    GoogleLoginView
)

urlpatterns = [
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('add-credits/', AddCreditsView.as_view(), name='add-credits'),
    path('purchase/', PurchaseDocumentView.as_view(), name='purchase'),
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),
]
