from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token

def root_view(request):
    return JsonResponse({
        'message': 'Welcome to the API Server',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/',
            'get_token': '/api-token-auth/',
            'books_list': '/api/books/',
            'books_crud': '/api/books_all/'
        }
    })

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
]