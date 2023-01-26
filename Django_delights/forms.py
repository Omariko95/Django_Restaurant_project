from django import forms
from .models import MenuItem , Ingredient , Purchase , RecipeRequirement


class IngredientForm(forms.ModelForm):
    class Meta:
        Model = Ingredient
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        Model = MenuItem
        fields = "__all__"


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        Model = RecipeRequirement
        fields = "__all__"

class PurchaseForm(forms.ModelForm):
    class Meta:
        Model = Purchase
        fields = "__all__"