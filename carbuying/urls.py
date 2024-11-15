from django.contrib import admin
from django.urls import path
from cars import views  # Import views from the app
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.car_list, name='car_list'),  # Home page showing the list of cars
    path('<int:pk>/', views.car_detail, name='car_detail'),  # Car details
    path('create/', views.car_create, name='car_create'),  # Create a car
    path('<int:pk>/update/', views.car_update, name='car_update'),  # Update a car
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
       path('', views.car_list, name='car_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Delete a car

