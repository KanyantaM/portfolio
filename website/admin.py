from django.contrib import admin
from .models import Blog, BlogComment, Owner, ProjectDetails, Skill, Service, Counter, Tag, Testimonial

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'icon')

class CounterAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'count', 'icon')

######## HOME ###############################
admin.site.register(Owner)
admin.site.register(Skill)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register(Testimonial)

########## BLOG #########################
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Tag)

########### PORTFOLIO
admin.site.register(ProjectDetails)