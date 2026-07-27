from rest_framework.generics import CreateAPIView
from .seriallizers import LoginSerializer, RefreshSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class RegisterAPIView(CreateAPIView):
    serializer_class=RegisterSerializer

class RegisterAPIView(generics):
    serializer_class=RegisterSerializer

class ProfileAPIView(APIView):

    permission_classes= [IsAuthenticated]

    def get(self, request):
        return Response({
            'username': request.user.username,
            'email': request.user.email
        })
    
class LogoutAPIView(APIView):

    permission_classes=[IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']

            token= RefreshToken(refresh_token)

            token.blacklist()

            return Response(
                {'message': 'Logout succesful'},
                status=status.HTTP_205_RESET_CONTENT
            )
        
        except Exception:
            return Response(
                {'error': 'Invalid refresh Token'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
class LoginAPIView(APIView):

    def post(self, request):
        serializer= LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class RefreshAPIView(APIView):

    def post(self, request):
        serializer= RefreshSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)