from django.contrib import admin
from services.models import service
class serviceadmin(admin.ModelAdmin):
    list_display = ('model_icon', 'model_title','description')
    search_fields=('name','description')
    class Meta:


# Register your models here