from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Account
from .serializers import AccountSerializer, AccountBalanceUpdateSerializer, LoginSerializer
from rest_framework import status, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from rest_framework.views import APIView
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Account
from .serializers import AccountSerializer, AccountBalanceUpdateSerializer, LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from rest_framework.views import APIView
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = AccountBalanceUpdateSerializer(instance, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['patch','post'], url_path='balance', url_name='update_balance')
    @csrf_exempt  # Add this line to disable CSRF protection
    def update_balance(self,request, pk=None):
        instance = self.get_object()
        serializer = AccountBalanceUpdateSerializer(instance, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True, methods=['get'], url_path='balance', url_name='get_balance')
    def get_balance(self, request, pk=None):
        account = self.get_object()
        return Response({'balance': account.balance})


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        # Generate token for the user
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        # Get the user authentication token
        token = request.auth
        if token:
            # delete the token
            token.delete()
            return Response({"message": "Logged out successfully."})
        else:
            return Response({"error": "No valid authentication token found."}, status=400)
