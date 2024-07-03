# Use djangorestframework-simplejwt for JWT authentication
# Install using:
# >> pip install djangorestframework-simplejwt

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# Create a token view for user authentication
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Generate a token for a user
def generate_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# To authenticate a user and get tokens
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# Use MyTokenObtainPairView to get tokens
# Pass username and password in the request
# Output will contain 'refresh' and 'access' tokens
# Please Like and Subscribe