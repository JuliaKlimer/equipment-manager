from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('openapi/', get_schema_view(
        title="Equipment Manager",
        description="Equipment Manager API documentation"
    ), name='openapi'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi'}
    ), name='swagger-ui'),
]
