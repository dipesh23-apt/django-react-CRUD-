"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django_minio_backend import MinioBackend
from graphene_django.views import GraphQLView
from file.schema import schema

minio_available = MinioBackend('').is_minio_available()  # An empty string is fine this time
if minio_available:
    print("MINIO SERVER running at 192.168.1.5:9001")
else:
    print("NOK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('api/v1/file/',include('file.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)