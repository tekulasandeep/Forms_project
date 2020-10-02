from django.urls import path
from django.contrib import admin

from detail import views as detail_views

urlpatterns = [
 path('', detail_views.user_list),
 path('userdetails/', detail_views.userdetails),

 path('admin/', admin.site.urls),
]
