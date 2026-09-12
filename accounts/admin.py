from django.contrib import admin
from .models import UserProfile, MissingChild,Alert


admin.site.register(UserProfile)
admin.site.register(MissingChild)
admin.site.register(Alert)