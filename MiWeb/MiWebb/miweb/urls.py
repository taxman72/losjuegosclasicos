from django.urls import path
from miweb.views import home,saludo,dame_fecha,calcula_edad,boton
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('', home,name='home'),
    path('saludo/', saludo),
    path('fecha/', dame_fecha),
    path('edades/<int:agno>', calcula_edad),
    path('boton/', boton),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)