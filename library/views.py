from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Document, Profile, Purchase
from .serializers import DocumentSerializer

class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        subject = self.request.query_params.get('subject')
        class_level = self.request.query_params.get('class_level')
        doc_type = self.request.query_params.get('doc_type')
        
        if subject:
            queryset = queryset.filter(subject=subject)
        if class_level:
            queryset = queryset.filter(class_level=class_level)
        if doc_type:
            queryset = queryset.filter(doc_type=doc_type)
            
        return queryset

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'detail': 'Email et mot de passe requis'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=email).exists():
            return Response({'detail': 'Cet email est déjà utilisé'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=email, email=email, password=password)
        profile = Profile.objects.create(user=user, full_name=full_name)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user': {
                'name': profile.full_name,
                'email': user.email,
                'credits': profile.credits
            }
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)
        if not user:
            return Response({'detail': 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        profile = user.profile

        return Response({
            'token': token.key,
            'user': {
                'name': profile.full_name,
                'email': user.email,
                'credits': profile.credits
            }
        })

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = user.profile
        return Response({
            'name': profile.full_name,
            'email': user.email,
            'credits': profile.credits
        })

class AddCreditsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        amount = request.data.get('amount', 0)
        profile = request.user.profile
        profile.credits += int(amount)
        profile.save()
        return Response({
            'message': 'Crédits ajoutés avec succès',
            'user': {
                'name': profile.full_name,
                'email': request.user.email,
                'credits': profile.credits
            }
        })

class PurchaseDocumentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        document_id = request.data.get('document_id')
        try:
            document = Document.objects.get(id=document_id)
        except Document.DoesNotExist:
            return Response({'detail': 'Document non trouvé'}, status=status.HTTP_404_NOT_FOUND)

        profile = request.user.profile
        
        # Check if already purchased
        if Purchase.objects.filter(user=request.user, document=document).exists():
             return Response({
                'pdfUrl': document.pdf_url,
                'price': 0,
                'user': {
                    'name': profile.full_name,
                    'email': request.user.email,
                    'credits': profile.credits
                }
            })

        if profile.credits < document.price:
            return Response({'detail': 'Crédits insuffisants'}, status=status.HTTP_400_BAD_REQUEST)

        profile.credits -= document.price
        profile.save()
        Purchase.objects.create(user=request.user, document=document)

        return Response({
            'pdfUrl': document.pdf_url,
            'price': document.price,
            'user': {
                'name': profile.full_name,
                'email': request.user.email,
                'credits': profile.credits
            }
        })

class GoogleLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        # Simulation d'une connexion Google
        return Response({'detail': 'Google Login non implémenté en mode réel, utilisez login classique'}, status=status.HTTP_501_NOT_IMPLEMENTED)
