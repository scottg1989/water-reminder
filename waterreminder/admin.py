from django.contrib import admin
from .models import User, Container, Log

admin.site.register(User)
admin.site.register(Container)
admin.site.register(Log)
