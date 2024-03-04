from django.contrib import admin
from .models import BookDetails,BookDetailsAdmin
admin.site.register(BookDetails,BookDetailsAdmin)
