from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializer import PostSerializer

@api_view(['GET'])
def getPost(request):
    app = Post.objects.all()
    serializer = PostSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)