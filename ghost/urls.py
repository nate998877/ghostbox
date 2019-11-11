"""ghost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from ghost import views
from ghost.models import BRoast

admin.site.register(BRoast)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.broast_form, name="add"),
    path('', views.homepage, name="homepage"),
    path('byvote', views.homepage, {"byvote":True}, name="byvote"),
    path('boasts', views.homepage, {"roasts":True}, name="boasts"),
    path('roasts', views.homepage, {"boasts":True}, name="roasts"),
    path('<int:pk>/<slug:vote>', views.homepage, name="upvote"),
    path('<int:pk>/<slug:vote>', views.homepage, name="downvote"),
]
