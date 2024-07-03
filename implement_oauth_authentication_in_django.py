# Use django-allauth for OAuth authentication
# Install django-allauth using
# >> pip install django-allauth

# Add 'allauth' and 'allauth.account' to INSTALLED_APPS in settings.py

# Include the allauth URLs in urls.py
urlpatterns = [
    path('accounts/', include('allauth.urls')),
]

# Configure authentication backends in settings.py
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Set up social application in Django admin
# Add social application with provider, client id, and secret

# Add social account provider to settings.py
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'your_client_id',
            'secret': 'your_secret',
            'key': ''
        }
    }
}

# Add LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_URL in settings.py
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# Please Like and Subscribe