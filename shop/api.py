
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'product', views.ProductListViewSet)
# router.register(r'order', views.OrderListView)
# router.register(r'employe', views.EmployesListView)