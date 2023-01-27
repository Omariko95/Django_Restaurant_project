from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('', views.HomeView.as_view() , name='home'),
  path('accounts/login/' , auth_views.LoginView.as_view(template_name = 'registration/login.html' , redirect_field_name = 'home'), name= "login"),
  path('logout/' , views.logout , name="logout"),
  path('ingredients/' , views.IngredientsView.as_view(), name ="ingredients"),
  path('ingredients/new', views.CreateIngredientsView.as_view(), name= "add_ingredient"),
  path('ingredients/<slug:pk>/update', views.UpdateIngredientView.as_view() , name= "update_ingredient"),
  path('ingredients/<slug:pk>/delete', views.DeleteIngredientView.as_view() , name= "delete_ingredient"),
  path('menu_list/', views.MenuView.as_view(), name= "menu"),
  path('menu_item/new', views.NewMenuItemView.as_view(), name= "new_menu_item"), 
  path('menu_item/<slug:pk>/update' , views.UpdateMenuItemView.as_view(), name= "update_menu_item"), 
  path('menu_item/<slug:pk>/delete', views.DeleteMenuItemView.as_view() , name= "delete_menu_item"), 
  path('reciperequirements/new' , views.NewRecipeRequirementView.as_view(), name= "new_recipe_requirement"),
  path('reciperequirements/<slug:pk>/update' , views.UpdateRecipeRequirementView.as_view(), name= "update_recipe_requirements"), 
  path('reciperequirements/<slug:pk>/delete', views.DeleteRecipeRequirementView.as_view(), name= "delete_recipe_requirements"),
  path('purchase/', views.PurchasesView.as_view(), name="purchase"),
  path('purchases/new', views.NewPurchaseView.as_view(), name="new_purchase"),
  path('reports', views.ReportView.as_view(), name= 'reports' )
]