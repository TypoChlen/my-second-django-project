from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from .views import RegisterView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),  # Обновленное имя функции
    path('profile/', views.profile_view, name='profile'),
    path('registration/', RegisterView.as_view(), {'next_page': 'profile'}, name='registration'),
    path('bomb', views.bomb, name='bomb'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
