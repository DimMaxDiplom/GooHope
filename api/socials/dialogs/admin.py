from django.contrib import admin
from .models import Dialog, Messages, Dialogs


class DialogAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'friend']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['dialog', 'message', 'sender']


class DialogsAdmin(admin.ModelAdmin):
    list_display = ['user', 'dialog']


admin.site.register(Dialog, DialogAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Dialogs, DialogsAdmin)
