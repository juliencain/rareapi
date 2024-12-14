"""View module for handling requests about posts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, Category, RareUser


class PostView(ViewSet):
    """View for handling post requests"""

    def retrieve(self, request, pk):
        """Handle GET request for single post"""
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all posts"""
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for creating a post"""
        try:
            rare_user = RareUser.objects.get(pk=request.data["rare_user_id"])
            category = Category.objects.get(pk=request.data["category_id"])
            
            post = Post.objects.create(
                rare_user=rare_user,
                category=category,
                title=request.data["title"],
                publication_date=request.data["publication_date"],
                image_url=request.data["image_url"],
                content=request.data["content"],
                approved=request.data.get("approved", True)
            )
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except RareUser.DoesNotExist:
            return Response({'message': 'Rare user not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response({'message': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
   



class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts"""
    
    class Meta:
        model = Post
        depth = 1
        fields = ('id', 'rare_user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')
