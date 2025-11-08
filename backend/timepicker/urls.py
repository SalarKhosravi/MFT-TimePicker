from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CalendarSlotViewSet, StudentPickViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'slots', CalendarSlotViewSet, basename='slot')
router.register(r'picks', StudentPickViewSet, basename='pick')

urlpatterns = router.urls
