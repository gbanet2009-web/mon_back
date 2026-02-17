from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserSerializer, CourseSerializer, ExerciseSerializer, BacSubjectSerializer
from .models import User, Course, Exercise, BacSubject
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Authenticate using email or username
        user = authenticate(request, username=email, password=password)
        if not user:
            # If email failed, try username (if your User model supports it, AbstractUser does)
            user = authenticate(request, username=User.objects.filter(email=email).first().username if User.objects.filter(email=email).first() else None, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user

class UpdateClassView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        class_id = request.data.get('classId')
        if not class_id:
            return Response({'message': 'classId is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        user.class_id = class_id
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

class AddCreditsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        if not amount or not isinstance(amount, int) or amount <= 0:
            return Response({'message': 'Valid amount is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        user.credits += amount
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        class_id = self.request.query_params.get('classId')
        if self.request.user.class_id == 'enseignant': # Assuming 'enseignant' can see all courses
            return Course.objects.all()
        elif class_id:
            return Course.objects.filter(class_id=class_id)
        return Course.objects.filter(class_id=self.request.user.class_id)

class ExerciseListView(generics.ListAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        class_id = self.request.query_params.get('classId')
        if self.request.user.class_id == 'enseignant': # Assuming 'enseignant' can see all exercises
            return Exercise.objects.all()
        elif class_id:
            return Exercise.objects.filter(class_id=class_id)
        return Exercise.objects.filter(class_id=self.request.user.class_id)

class BacSubjectListView(generics.ListAPIView):
    serializer_class = BacSubjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return BacSubject.objects.all()