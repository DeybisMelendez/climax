from django.urls import path
from .views import settings_view, restore_backup, delete_backup, create_backup

urlpatterns = [
    path('', settings_view, name='settings'),
    path("backup/create/", create_backup, name="backup"),
    path('backup/restore/<str:backup_name>/',
         restore_backup, name='restore_backup'),
    path('backup/delete/<str:backup_name>/',
         delete_backup, name='delete_backup'),
]
