from django.contrib import admin
from .models import Students, Scores

# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Scores)
class ScoreAdmin(admin.ModelAdmin):
    pass