from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated


from . import models
from . import permissions
from . import serializers

# Create your views here.
class Hello_Api(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self,request,format = None):
        """Returns a list of api view features"""
        api_bill = [
        "Made in Lagos",
        "#ENDSARS",
        "#LEKKITOLLGATE",
        "Pray For Nigeria"
        ]
        return Response({"messages": "an_api","an_apiView": api_bill})

    def post(self,request):
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """This method updates an object in the APIView"""



        return Response({"method":"put"})

    def patch(self,request,pk=None):
        """This method partially updates the object in the APIView"""



        return Response({"method":"patch"})

    def delete(self,request,pk=None):
        """This method deletes the object in the APIView"""


        return Response({"method":"delete"})


class HelloViewSets(viewsets.ViewSet):
    """This docstring test our viewSet"""
    serializer_class =serializers.HelloSerializer

    def list(self,request):
        a_viewSet= [
        'viewset provides less code and more functionalities',
        'provides list,create,update,partially update our api view',
        'automatically maps URLs using Routes'
        ]

        return Response({'message':'apiMessage','a_viewSet':a_viewSet})

    def create(self,request):
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk =None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method': "PUT"})

    def partial_update(self,request,pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """This class creates,reads and update our user profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):
    """This class creates a login end point,checks email and password and returns a token """

    serializer_class = AuthTokenSerializer
    def create(self,request):

        return ObtainAuthToken().post(request)


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    authentication_classes =(TokenAuthentication,)
    serializer_class =serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)
    def perform_create(self,serializer):
        serializer.save(user_profile = self.request.user)
