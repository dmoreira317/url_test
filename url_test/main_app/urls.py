from rest_framework import routers
from main_app.views import MeasureResponseViewSet

router = routers.DefaultRouter()
router.register(r'measure', MeasureResponseViewSet, basename='measure-response')

urlpatterns = router.urls
