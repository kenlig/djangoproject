from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Award
# Register your models here.
class AwardAdmin(admin.ModelAdmin):
    list_display=['description','photo']

admin.site.register(Award,AwardAdmin)

admin.site.site_header='企业后台管理系统'
admin.site.site_title='企业后台管理系统'