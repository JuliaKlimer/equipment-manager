from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-status', views.add_status, name='add-status'),
    path('add-type', views.add_type, name='add-type'),
    path('add-producer', views.add_producer, name='add-producer'),
    path('add-human', views.add_human, name='add-human'),
    path('add-equipment', views.add_equipment, name='add-equipment'),
    path('add-ownership', views.add_ownership, name='add-ownership'),
    path('<int:pk>/equipment-detail', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('<int:pk>/human-detail', views.HumanDetailView.as_view(), name='human-detail'),
    path('<int:pk>/producer-detail', views.ProducerDetailView.as_view(), name='producer-detail'),
    path('<int:pk>/type-detail', views.TypeDetailView.as_view(), name='type-detail'),
    path('<int:pk>/ownership-detail', views.OwnershipDetailView.as_view(), name='ownership-detail'),
    path('<int:pk>/status-detail', views.StatusDetailView.as_view(), name='status-detail'),
    path('<int:pk>/equipment-update', views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('<int:pk>/human-update', views.HumanUpdateView.as_view(), name='human-update'),
    path('<int:pk>/producer-update', views.ProducerUpdateView.as_view(), name='producer-update'),
    path('<int:pk>/type-update', views.TypeUpdateView.as_view(), name='type-update'),
    path('<int:pk>/ownership-update', views.OwnershipUpdateView.as_view(), name='ownership-update'),
    path('<int:pk>/status-update', views.StatusUpdateView.as_view(), name='status-update'),
    path('<int:pk>/equipment-delete', views.EquipmentDeleteView.as_view(), name='equipment-delete'),
    path('<int:pk>/human-delete', views.HumanDeleteView.as_view(), name='human-delete'),
    path('<int:pk>/producer-delete', views.ProducerDeleteView.as_view(), name='producer-delete'),
    path('<int:pk>/type-delete', views.TypeDeleteView.as_view(), name='type-delete'),
    path('<int:pk>/ownership-delete', views.OwnershipDeleteView.as_view(), name='ownership-delete'),
    path('<int:pk>/status-delete', views.StatusDetailView.as_view(), name='status-delete')
]