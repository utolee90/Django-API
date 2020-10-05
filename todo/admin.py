from django.contrib import admin
from .models import TodoGroup, Todo, FavouriteGroup, Favourite

# Register your models here.
@admin.register(TodoGroup)
class TodoGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

@admin.register(FavouriteGroup)
class FavouriteGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    pass
