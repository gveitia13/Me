from django.conf.urls.static import static
from django.urls import path

from Ropa import settings
from apk.views import wash

app_name = 'apk'
urlpatterns = [
    path('admin/apk/clothing/', wash, name='lavar'),
]
