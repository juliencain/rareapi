"""View module for handling requests about rare users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser


class RareUserView(ViewSet):
    """rare rare user view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single rare user
      
        Returns:
            Response -- JSON serialized rare user
        """

        try:
            rareUser = RareUser.objects.get(pk=pk)
            serializer = RareUserSerializer(rareUser)
            return Response(serializer.data)
        except RareUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all rare users

        Returns:
            Response -- JSON serialized list of rare users
        """
        rareUsers = RareUser.objects.all()

        serializer = RareUserSerializer(rareUsers, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized rare user instance
         """

        rareUser = RareUser.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            bio=request.data["bio"],
            profile_image_url=request.data["profile_image_url"],
            email=request.data["email"],
            created_on=request.data["created_on"],
            active=request.data["active"],
            is_staff=request.data["is_staff"],
            uid=request.data["uid"]
        )
        serializer = RareUserSerializer(rareUser)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
      """Handle PUT requests for updating a rare user

      Returns:
        Response -- JSON serialized rare user instance with 200 status
      """
      try:
          # Fetch the artist by primary key
          rareUser = RareUser.objects.get(pk=pk)

          # Update fields
          rareUser.first_name = request.data["first_name"]
          rareUser.last_name = request.data["last_name"]
          rareUser.bio = request.data["bio"]
          rareUser.profile_image_url = request.data["profile_image_url"]
          rareUser.email = request.data["email"]
          rareUser.created_on = request.data["created_on"]
          rareUser.active = request.data["active"]
          rareUser.is_staff = request.data["is_staff"]
          rareUser.uid = request.data["uid"]
          rareUser.save()

          # Serialize the updated rare user
          serializer = RareUserSerializer(rareUser)

          # Return updated rare user data with 200 OK
          return Response(serializer.data, status=status.HTTP_200_OK)
      except RareUser.DoesNotExist:
        return Response(
            {"message": "Rare User not found."},
            status=status.HTTP_404_NOT_FOUND)
        
      except KeyError as e:
        return Response(
            {"message": f"Missing required field: {e.args[0]}"},
            status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self, request, pk):
        rareUser = RareUser.objects.get(pk=pk)
        rareUser.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users
    """
    
    class Meta:
        model = RareUser
        depth = 1
        fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid')
