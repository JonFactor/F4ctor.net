from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

from .models import User, UserSerializer

def getUser(request):
    
    token = request.COOKIES.get('jwt')
    
    if token == None:
        return None
    if "=" in token:
        token = token.split("=")[0]
    if ";" in token:
        token = token.split(";")[1]

    if not token:
        raise AuthenticationFailed('Unauthenticated')
        
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('jwt expired signature')

    return User.objects.filter(id=payload['id']).first()

# Create your views here.
class UserView(APIView):
    def post(self, request): # 'name', 'firstName', 'lastName', 'email', 'password', 'profilePic', 'description', 'phoneNum']
        request.data.update({"description":"nothing to see here"})
        request.data.update({"profilePic":"http://www.gravatar.com/avatar"})
    
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request): # requType
        
        if request.query_params["requType"] == "SELF":
            user = getUser(request)
            if user == None:
                return Response(status=400)
            serializer = UserSerializer(user)

            return Response(serializer.data)
        
        elif request.query_params["requType"] == "ID":
            id = request.query_params["id"] # id
            
            user = User.objects.filter(id=id).first()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        return Response({"message":"incorrect enum requType"}, staus=401)   
    
#------------------------------------------------- Login View ---------
#   
#     Purpose:  
#             - post
#             To authorize the user to access the database.
#             
#     Input / Params:  
#             - post
#             requType -> COOKIES: jwt -> string, CREDENTIALS -> email / password -> string / filters
#                
#-------------------------------------------------------------------------
    
class LoginView(APIView):
    def post(self, request): # requType
        
        if request.data['requType'] == "COOKIES": #JWT
            token = request.data['jwt']
            response = Response()
            response.set_cookie(key="jwt", value=token, httponly=True)

            response.data = {
                "jwt": token
            }
            
            return response
        
        elif request.data['requType'] == 'CREDENTIALS':
            email = request.data['email']
            password = request.data['password']

            user = User.objects.filter(email=email).first()
            if user is None:
                raise AuthenticationFailed('User not found')

            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password')

            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret',
                            algorithm='HS256')

            response = Response()

            response.set_cookie(key="jwt", value=token, httponly=True)

            response.data = {
                "jwt": token
            }

            return response
        
        return Response({"message":"incorrect enum requType"}, staus=401)
