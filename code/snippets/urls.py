from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]