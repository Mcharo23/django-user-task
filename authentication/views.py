from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serializers import UserSerializer

from .models import User

import bcrypt

import jwt
import datetime

import environ
env = environ.Env()
environ.Env.read_env()


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/auth/',
        '/auth/register/',
        '/auth/logout/',
        '/task/',
        '/task/create-task',
        '/task/update-status/',
        '/task/delete-task/',
    ]
    return Response(routes)


def AuthorizeUser(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = User.objects.get(user_id=payload['user_id'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')

    return user


def _hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14)).decode('utf-8')


class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data['password']
        serializer.validated_data['password'] = _hash_password(
            password=password)
        serializer.save()

        return Response(serializer.data)


class LoginView(APIView):

    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed()

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise AuthenticationFailed()

        payload = {
            'user_id': str(user.user_id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40),
            'iat': datetime.datetime.utcnow()

        }

        token = jwt.encode(payload, env('SECRET_KEY'), algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'token': token, }

        return response


class UserView(APIView):
    def get(self, request):

        user = AuthorizeUser(request)
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Successfully logged out',
        }

        return response
