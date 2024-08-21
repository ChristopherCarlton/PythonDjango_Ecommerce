from django.urls import path
# from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from rest_framework_nested import routers, NestedDefaultRouter

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('revies', views.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls
