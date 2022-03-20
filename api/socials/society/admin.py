from django.contrib import admin
from .models import User, Society, SocietyMembers, SocietyComments

admin.site.register(User)
admin.site.register(Society)
admin.site.register(SocietyMembers)
admin.site.register(SocietyComments)
