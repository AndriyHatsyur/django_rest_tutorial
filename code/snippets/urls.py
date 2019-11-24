from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name ='snippets-list' ),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name = 'users-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('snippets/highlight/<int:pk>/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]