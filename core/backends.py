from firebase_admin import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        id_token = auth_header.split(' ').pop()
        try:
            decoded_token = auth.verify_id_token(id_token)
        except:
            raise exceptions.AuthenticationFailed('Invalid ID token')

        email = decoded_token.get('email')
        if not email:
            raise exceptions.AuthenticationFailed('No email found in token')

        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            user = User.objects.create(
                username=email,
                email=email,
                password=make_password(None)
            )

        return (user, None)
