from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, status
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import Task
from core.jwttoken import generate_access_token, generate_refresh_token
from rest_framework.response import Response

## Login APIView Here.
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerilaizer
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            response = Response()
            ## check email and password
            if (email is None) or (password is None):
                context = {'status': False,'message': 'Invalid credentials. Please try again'}
                return Response(context, status=status.HTTP_200_OK)

            user = User.objects.filter(email=email).first()

            if(user is None):
                context = {'status': False,'message': 'Email address incorrect.'}
                return Response(context, status=status.HTTP_200_OK)

            if (not user.check_password(password)):
                context = {'status': False,'message': 'Wrong password'}
                return Response(context, status=status.HTTP_200_OK)
            
            access_token = generate_access_token(user.id)
            refresh_token = generate_refresh_token(user.id)
            response.data = {'status': True, 'massage': 'Login Successfully',"access_token": access_token,"refresh_token": refresh_token,}
            return response

        except Exception as e:
            context = {'status': False, 'message': 'Something Went Wrong'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



## Task Model VIew Sets.
class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-created_on')
    