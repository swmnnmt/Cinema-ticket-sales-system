"""Cinema_ticket_sales_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # if admin is at the first of url go to default django admin
    path('admin/', admin.site.urls),
    # if ticketing is at the first of url go to urls file in ticketing app
    path('ticketing/', include('ticketing.urls')),
    path('accounts/', include('accounts.urls')),
]
# following code will serve image files when we are in debug mode in  localhost
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
