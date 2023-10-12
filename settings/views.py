import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.management import call_command
from django.shortcuts import render
from dbbackup import management as dbbackup_management


def settings_view(request):
    backup_files = os.listdir(settings.DBBACKUP_STORAGE_OPTIONS['location'])
    return render(request, "settings/settings.html", {'backup_files': backup_files})


def create_backup(request):
    call_command('dbbackup')
    return redirect("settings")


def restore_backup(request, backup_name):
    # TODO: Agregar funcionalidad
    # call_command('dbrestore', os.path.join(
    #    settings.DBBACKUP_STORAGE_OPTIONS['location'], backup_name))
    return redirect('settings')


def delete_backup(request, backup_name):
    os.remove(os.path.join(
        settings.DBBACKUP_STORAGE_OPTIONS['location'], backup_name))
    return redirect('settings')
