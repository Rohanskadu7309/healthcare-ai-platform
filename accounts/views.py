from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse

from common.responses import APIResponse

from .serializers import RegisterSerializer, LoginSerializer, RefreshTokenSerializer, LogoutSerializer, ProfileSerializer
from .services import RegistrationService, LoginService, RefreshTokenService, LogoutService, ProfileService



class RegisterAPIView(APIView):

    authentication_classes = []
    permission_classes = []
    
    @extend_schema(
        tags=["Authentication"],
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

        return APIResponse.success(
            message="User registered successfully.",
            data={
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            status_code=status.HTTP_201_CREATED,
        )
        

class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    @extend_schema(
        tags=["Authentication"],
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(description="Login successful."),
            400: OpenApiResponse(description="Validation Error"),
        },
    )
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = LoginService.login(serializer.validated_data)

        return APIResponse.success(
            message="Login successful.",
            data={
                "access": result["access"],
                "refresh": result["refresh"],
                "user": {
                    "id": result["user"].id,
                    "email": result["user"].email,
                    "first_name": result["user"].first_name,
                    "last_name": result["user"].last_name,
                },
            },
        )
        

class RefreshTokenAPIView(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    @extend_schema(
        tags=["Authentication"],
        request=RefreshTokenSerializer,
        responses={
            200: OpenApiResponse(description="Access token refreshed successfully."),
            400: OpenApiResponse(description="Invalid or expired refresh token."),
        },
    )
    
    def post(self, request):
        
        serializer = RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        result = RefreshTokenService.refresh(serializer.validated_data)

        return APIResponse.success(
            message="Access token refreshed successfully.",
            data=result,
        )
        

class LogoutAPIView(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    @extend_schema(
        tags=["Authentication"],
        request=LogoutSerializer,
        responses={
            200: OpenApiResponse(description="Logout successful."),
            400: OpenApiResponse(description="Validation error")
        }
    )
    
    def post(self, request):
        
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        LogoutService.logout(serializer.validated_data)
        
        return APIResponse.success(
            message="Logout successful.",
        )
        

class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Authentication"],
        responses={
            200: OpenApiResponse(description="Profile retrieved successfully."),
            401: OpenApiResponse(description="Authentication failed."),
        },
    )
    
    def get(self, request):
        
        user = ProfileService.get_profile(request.user)

        serializer = ProfileSerializer(user)

        return APIResponse.success(
            message="Profile retrieved successfully.",
            data=serializer.data,
        )