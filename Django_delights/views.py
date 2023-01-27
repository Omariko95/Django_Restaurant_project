from django.shortcuts import render , redirect 
from django.views.generic import ListView , CreateView
from django.views.generic.base import TemplateView , TemplateResponseMixin , RedirectView
from django.views.generic.edit import UpdateView , DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login , authenticate
from django.contrib.auth.decorators import login_required
from .forms import IngredientForm , RecipeRequirementForm , MenuItemForm , PurchaseForm
import random
from .models import Ingredient,MenuItem,RecipeRequirement,Purchase
from django.urls import reverse_lazy
from django.db.models import Sum , F 



# Create your views here.
class HomeView(TemplateView):
    template_name = "Django_delights/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context



#Let's work with Ingredients

class IngredientsView(LoginRequiredMixin , ListView):
    model = Ingredient
    template_name = 'Django_delights/view_ingredients.html'


class CreateIngredientsView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name ="Django_delights/add_ingredient.html"
    form_class = IngredientForm

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "Django_delights/update_ingredient.html"
    form_class = IngredientForm


class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "Django_delights/delete_ingredient.html"
    form_class = IngredientForm
    success_url = "/ingredients"

#Now let's move on to the MenuItem model:

class MenuView(LoginRequiredMixin, ListView):

    template_name = "Django_delights/menu_list.html"
    model = MenuItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_dict = {}

        for item in MenuItem.objects.all():
            total_cost = 0 
            for req in item.reciperequirement_set.all():
                total_cost += req.req_cost()
            total_dict[req.id] = {'total_cost': round(total_cost, 2),'profit_cost':round(req.price - total_cost, 2)}
        context["total_dict"] = total_dict
        return context 


class NewMenuItemView(LoginRequiredMixin, CreateView):
    template_name = "/Django_delights/add_menu_item.html"
    model = MenuItem
    form_class = "MenuItemForm"

class UpdateMenuItemView(LoginRequiredMixin, UpdateView):
    template_name = "/Django_delights/update_menu_item.html"
    model = MenuItem
    form_class = "MenuItemForm"
    success_url = "/menu"
    
    

class DeleteMenuItemView(LoginRequiredMixin, DeleteView):
    template_name = "/Django_delights/delete_menu_item.html"
    model = MenuItem
    form_class = "MenuItemForm"
    success_url = "/menu"


#Let's handle some recipe requirements 


class NewRecipeRequirementView(LoginRequiredMixin , CreateView):
    template_name = "Django_delights/add_recipe_requirement"
    model = RecipeRequirement
    form_class = RecipeRequirementForm

class UpdateRecipeRequirementView(LoginRequiredMixin, UpdateView):
    template_name = "Django_delights/update_recipe_requirement"
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    success_url ="/menu"

class DeleteRecipeRequirementView(LoginRequiredMixin, DeleteView):
    template_name = "Django_delights/delete_recipe_requirement"
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    success_url = "/menu"

#Lastly we will create the Purchaseview

class PurchasesView(LoginRequiredMixin, ListView):
    template_name = "Django_delights/purchase_list.html"
    model = Purchase


class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = "Django_delights/add_purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["potion_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")


class ReportView(LoginRequiredMixin, TemplateView):

    template_name = "/Django_delights/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.menu_item.price *\
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context

#Define login and logout functions below


def logout(request):
    logout(request)
    return redirect("home")


def login(request):
    return redirect('')

