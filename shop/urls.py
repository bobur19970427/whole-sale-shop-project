from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
    path('order/', views.OrderListView.as_view()),
    path('order/<int:pk>/', views.OrderDetailView.as_view()),
    path('employe/', views.EmployesListView.as_view()),
    path('employe/<int:pk>/', views.EmployeDetailView.as_view()),
]