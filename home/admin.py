from django.contrib import admin
from .models import Intro, Services, Works, Testi

# Register your models here.
class IntroAdmin(admin.ModelAdmin):
    list_display = ('ijudul', 'iisi','ifoto',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('sjudul','sisi','sfoto', )

class WorksAdmin(admin.ModelAdmin):
    list_display = ('wfoto',)

class TestiAdmin(admin.ModelAdmin):
    list_display = ('tnama','tisi',)


admin.site.register(Intro, IntroAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Works, WorksAdmin)
admin.site.register(Testi, TestiAdmin)

