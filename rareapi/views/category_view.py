from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category


class CategoryView(ViewSet):
    """Rare api category view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category
        Returns:
            Response -- JSON serialized category
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all categories
        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized category instance
        """
        category = Category.objects.create(
            label=request.data["label"],
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)  


    def update(self, request, pk):
        """Handle PUT requests for category
        Returns:
            Response -- Empty body with 204 status code
        """

        id = pk
        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]
        category.save()
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """ 
    class Meta:
        model = Category
        fields = ('id', 'label')
        depth = 1
