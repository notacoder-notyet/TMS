from rest_framework import routers

from .views import GlobalTaskViewSet, ObjectivesViewSet

app_name = 'task_manager'

router = routers.SimpleRouter()
router.register(r'global-task', GlobalTaskViewSet)
router.register(r'objectives', ObjectivesViewSet)

urlpatterns = router.urls
