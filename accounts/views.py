from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import RegisterSerializer
from .services import RegistrationService


class RegisterAPIView(APIView):

    authentication_classes = []
    permission_classes = []
    
    @extend_schema(
        request=RegisterSerializer,
        responses={
            201: OpenApiResponse(
                description="User registered successfully."
            ),
            400: OpenApiResponse(
                description="Validation Error"
            ),
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