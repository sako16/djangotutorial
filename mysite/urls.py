from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Bu satırı ekleyin: Boş yolu 'polls' uygulamasına yönlendirir.
    path('', include('polls.urls')), # VEYA 'polls/' yerine

    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]