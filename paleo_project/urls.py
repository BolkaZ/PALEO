from django.urls import path
from app import views
from app.views import index, getDetailPage, bid_view, add_to_bid
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', getDetailPage, name='getDetailPage'),
    path('bid/', bid_view, name='bid'),
    path('add-to-bid/<int:period_id>/', views.add_to_bid, name='add_to_bid'), # Новый путь для добавления в заявку
    path('admin/', admin.site.urls),
]
