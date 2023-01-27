from django.forms import ModelForm
from .models import MenuItem , Ingredient , Purchase , RecipeRequirement


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class RecipeRequirementForm(ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"