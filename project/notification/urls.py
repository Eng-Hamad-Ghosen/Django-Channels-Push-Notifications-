from django.urls import path
from notification import views
urlpatterns = [
    path('', views.notification_page_view, name='notification_page_view')
]
