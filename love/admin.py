# love/admin.py
from django.contrib import admin
from .models import LoveCard, Letter

admin.site.register(LoveCard)
admin.site.register(Letter)
