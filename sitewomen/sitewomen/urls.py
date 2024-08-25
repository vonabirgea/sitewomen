"""
URL configuration for sitewomen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from sitewomen import settings
from women.views import *
from rest_framework import routers
from django.conf.urls.static import static


# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$', 
#                       mapping={'get': 'list'}, 
#                       name='{basename}-list', 
#                       detail=False, 
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$', 
#                       mapping={'get': 'retrieve'}, 
#                       name='{basename}-detail', 
#                       detail=True, 
#                       initkwargs={'suffix': 'Detail'}),
#     ]


# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename="women")
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path('users/', include('users.urls', namespace="users")),
    path("__debug__/", include("debug_toolbar.urls")),
    # path("api/v1/", include(router.urls)),    # http://127.0.0.1:8000/api/v1/women/
    path("api/v1/drf-auth/", include('rest_framework.urls')),
    path("api/v1/women/", WomenAPIList.as_view()),
    path("api/v1/women/<int:pk>/", WomenAPIUpdate.as_view()),
    path("api/v1/womendelete/<int:pk>/", WomenAPIDestroy.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщины мира"
