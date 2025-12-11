from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import (
    PostSerializer, 
    PostDetailSerializer,
    CommentSerializer
)
from django.contrib.auth import get_user_model

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing posts.
    """
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by title/content if search parameter provided
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                title__icontains=search
            ) | queryset.filter(
                content__icontains=search
            )
        return queryset.distinct()
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        post_id = self.request.query_params.get('post', None)
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset