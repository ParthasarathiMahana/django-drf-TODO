from . import serializers, models
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TodosViewset(APIView):
    def get(self, request, id=None):
        todos = models.Todos.objects.all()
        serializer = serializers.TodosSerializer(todos, many=True)
        return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = serializers.TodosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        item = models.Todos.objects.get(id=id)
        serializer = serializers.TodosSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        item = models.Todos.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status":"success", "item":"Item deleted"})