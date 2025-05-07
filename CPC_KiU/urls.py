"""
URL configuration for CPC_KiU project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from root import views

#মিডিয়া দেখানোর জন্য এই ২ টা লাগবে 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('current_panel/', views.current_panel, name='current_panel'),
    path('former_panel_1/', views.former_panel_1, name='former_panel_1'),
    path('former_panel_2/', views.former_panel_2, name='former_panel_2'),
    path('current_faculty/', views.current_faculty, name='current_faculty'),
    path('former_faculty/', views.former_faculty, name='former_faculty'),
    path('event_details/<int:id>/', views.event_details, name='event_details'),
    path('course_details/<int:id>/', views.course_details, name='course_details'),
    path('contact/', views.contact_view, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
