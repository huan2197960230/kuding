
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notice/', views.notice),
    path('help/', views.help),
    path('tool/', views.tool),
    path('test/', views.test),
]

