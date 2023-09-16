from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),  # Use Django's LoginView
    path('logout/', LogoutView.as_view(), name='logout'),  # Use Django's LogoutView
    path('', views.home, name='home'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('place_order/', views.place_order, name='place_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

