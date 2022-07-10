from rest_framework import routers

from cart_order.views import CartViewSet, OrderViewSet

app_name = 'cart_order'

router = routers.SimpleRouter()
router.register(r'cart', CartViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = router.urls
