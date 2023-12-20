 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MEMO_APP.urls')),
    path('',include('REGISTRATION_APP.urls')),
]
