from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_data/', include('get_data.urls')),
    path('representation/', include('representation.urls'))
]
