from django.urls import path
from shopapp  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('checkout/',views.checkout, name='checkout'),
]
