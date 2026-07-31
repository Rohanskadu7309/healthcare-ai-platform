from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import RegisterSerializer, LoginSerializer, RefreshTokenSerializer
from .services import RegistrationService, LoginService, RefreshTokenService


class RegisterAPIView(APIView):

    authentication_classes = []
    permission_classes = []
    
    @extend_schema(
        request=RegisterSerializer,
        responses={
            201: OpenApiResponse(description="User registered successfully."),
            400: OpenApiResponse(description="Validation Error"),
        },
    )
    
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = RegistrationService.register(
            serializer.validated_data
        )

        return Response(
            {
                "success": True,
                "message": "User registered successfully.",
                "data": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
            },
            status=status.HTTP_201_CREATED,
        )
        

class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    @extend_schema(
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(description="Login successful."),
            400: OpenApiResponse(description="Validation Error"),
        },
    )
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = LoginService.login(serializer.validated_data)
        except ValueError as exc:
            return Response(
                {
                    "success": False,
                    "message": str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "data": {
                    "access": result["access"],
                    "refresh": result["refresh"],
                    "user": {
                        "id": result["user"].id,
                        "email": result["user"].email,
                        "first_name": result["user"].first_name,
                        "last_name": result["user"].last_name,
                    },
                },
            },
            status=status.HTTP_200_OK,
        )
        

class RefreshTokenAPIView(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    @extend_schema(
        request=RefreshTokenSerializer,
        responses={
            200: OpenApiResponse(description="Access token refreshed successfully."),
            400: OpenApiResponse(description="Invalid or expired refresh token."),
        },
    )
    
    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            result = RefreshTokenService.refresh(serializer.validated_data)
            
        except ValueError as e:

            return Response(
                {
                    "success": False,
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "success": True,
                "message": "Access token refreshed successfully.",
                "data": result,
            },
            status=status.HTTP_200_OK,
        )