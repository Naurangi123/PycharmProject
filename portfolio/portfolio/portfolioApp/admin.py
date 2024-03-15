from django.contrib import admin
from portfolioApp.models import Project,Data

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)

admin.site.register(Data)