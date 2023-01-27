from django.contrib import admin

from .models import Purchase, RecipeRequirement, MenuItem, Ingredient

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)