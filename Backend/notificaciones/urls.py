from django.urls import path
from . import views

urlpatterns = [
    # URL for retrieving all notifications for a user
    path('notifications/', views.NotificationListView.as_view(), name='notification-list'),

    # URL for marking a notification as read
    path('notifications/<int:pk>/mark-as-read/', views.NotificationMarkAsReadView.as_view(), name='notification-mark-as-read'),

    # URL for deleting a notification
    path('notifications/<int:pk>/delete/', views.NotificationDeleteView.as_view(), name='notification-delete'),
]
