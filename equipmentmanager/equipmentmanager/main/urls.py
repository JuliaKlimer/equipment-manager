from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='home'),
    path('add-status', views.add_status, name='add-status'),
    path('add-type', views.add_type, name='add-type'),
    path('add-producer', views.add_producer, name='add-producer'),
    path('add-human', views.add_human, name='add-human'),
    path('add-equipment', views.add_equipment, name='add-equipment'),
    path('add-ownership', views.add_ownership, name='add-ownership'),
    path('equipment-list/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('equipment-list/<int:pk>/equipment-detail', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('human-list/', views.HumanListView.as_view(), name='human-list'),
    path('human-list/<int:pk>/human-detail', views.HumanDetailView.as_view(), name='human-detail'),
    path('producer-list/', views.ProducerListView.as_view(), name='producer-list'),
    path('producer-list/<int:pk>/producer-detail', views.ProducerDetailView.as_view(), name='producer-detail'),
    path('type-list/', views.TypeListView.as_view(), name='type-list'),
    path('type-list/<int:pk>/type-detail', views.TypeDetailView.as_view(), name='type-detail'),
    path('ownership-list/', views.OwnershipListView.as_view(), name='ownership-list'),
    path('ownership-list/<int:pk>/ownership-detail', views.OwnershipDetailView.as_view(), name='ownership-detail'),
    path('status-list/', views.StatusListView.as_view(), name='status-list'),
    path('status-list/<int:pk>/status-detail', views.StatusDetailView.as_view(), name='status-detail'),
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
    path('<int:pk>/status-delete', views.StatusDetailView.as_view(), name='status-delete'),
    path("api/status/<int:pk>/", api.StatusDetail.as_view(), name="status_api"), #by id
    path("api/type/<int:pk>/", api.TypeDetail.as_view(), name="type-api"),  # by id
    path("api/equipment/<int:pk>/", api.EquipmentDetail.as_view(), name="equipment-api"),  # by id
    path("api/producer/<int:pk>/", api.ProducerDetail.as_view(), name="producer-api"),  # by id
    path("api/human/<int:pk>/", api.HumanDetail.as_view(), name="human-api"), #by id
    path("api/ownership/<int:pk>/", api.OwnershipDetail.as_view(), name="ownership-api"), #by id
    path("api/status/", api.StatusView.as_view(), name="status-api-view"), #all
    path("api/type/", api.TypeView.as_view(), name="type-api-view"),  # all
    path("api/equipment/", api.EquipmentView.as_view(), name="equipment-api-view"),  # all
    path("api/producer/", api.ProducerView.as_view(), name="producer-api-view"),  # all
    path("api/human/", api.HumanView.as_view(), name="human-api-view"), #all
    path("api/ownership/", api.OwnershipView.as_view(), name="ownership-api-view"), #all
]