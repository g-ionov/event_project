from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from event_app.views import OrganizationCreateView, EventViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Event app API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="ionov@lakriz.ru"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

router = routers.DefaultRouter()
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('organization/', OrganizationCreateView.as_view(), name='organization-create'),
    path('', include(router.urls)),
]
