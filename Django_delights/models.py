from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
#Let's create a list of ingredients and their respective quantities and prices

class MenuItem(models.Model):
    DOUBLE_CHEESEBURGER = "DC"
    SALAD = "SD"
    BUTTER_CHICKEN = "BC"
    TACO = "TO"
    BURRITO = "BO"
    SUNNYSIDEUP_EGGS = "SS"
    STRAWBERRYKIWI_CHEESECAKE = "SC"
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    SUPERSIZED = 'SS'

    SIZE_CHOICES = [ 
        (SMALL , 'Small') , (MEDIUM , 'Medium') , 
        (LARGE , 'Large') , (SUPERSIZED , 'SuperSized')
    ]

    MENU_CHOICES = [
        (DOUBLE_CHEESEBURGER , "Double_Cheeseburger") , (SALAD , "Salad") , (TACO, "Taco") , (BURRITO, "Burrito") , 
        (SUNNYSIDEUP_EGGS, "SunnySideup Eggs") , (STRAWBERRYKIWI_CHEESECAKE , "StrawberryKiwi Cheesecake")
    ]

    menu_choice = models.CharField(max_length=20 , choices = MENU_CHOICES )
    size = models.CharField(max_length= 2 , choices=SIZE_CHOICES , default= MEDIUM)
    price = models.FloatField(default= 0.00)
    description = models.CharField(max_length= 100)

    def get_absolute_url(self):
        return "/menu"
    
    def __str__(self):
        return f"""
        You have picked a {self.SIZE_CHOICES} serving of {self.MENU_CHOICES},
        the total cost is {self.price} $ 
        """
    def available(self):
        
        return all(recipe.enough() for recipe in self.reciperequirement_set.all())


class Ingredient(models.Model):
    OLIVE_OIL = "Olive Oil"
    FLOUR = "Flour"
    BUTTER = "Butter"
    CHICKEN = "Chicken"
    SUGAR = "Sugar"
    SALT = "Salt"
    EGG = "Egg"
    RICE = "Rice"
    BEEF = "Beef"
    ONION = "Onion"
    LETTUCE = "Lettuce"
    TOMATO = "Tomato"
    PICKLES = "Pickles"
    RELISH = "Relish"
    CUCUMBER = "Cucumber"
    BLUEBERRY = "Blueberry"
    BANANAS = "Bananas"
    STRAWBERRY = "Strawberry"
    KIWI = "Kiwi"
    CHEESE ="Cheese"


    INGREDIENT_CHOICES = [
        (OLIVE_OIL , "Olive oil") , (FLOUR , "Flour") , (BUTTER , "Butter"), (CHICKEN, "Chicken") ,(SUGAR , "Sugar") , 
        (SALT , "Salt"), (EGG , "Egg"), (RICE , "Rice"),(BEEF , "Beef") , (ONION , "Onion"), (LETTUCE , "Lettuce") , 
        (TOMATO , "Tomato") , (PICKLES ,"Pickles") ,(RELISH, "Relish") , (CUCUMBER, "Cucumber") , (BLUEBERRY, "Blueberry"),
        (BANANAS, "Bananas") , (STRAWBERRY, "Strawberry") , (KIWI , "Kiwi") , (CHEESE , "CE")
    ]
    Ingredient_name = models.CharField(max_length= 20 , choices = INGREDIENT_CHOICES)
    Ingredient_quantity = models.FloatField(default=0)
    Ingredient_price = models.FloatField(default=0)


    def get_absolute_url(self):
        return "/ingredients"


    
    def __str__(self):
        return f"""
        The Ingredient {self.Ingredient_name} is available for { self.Ingredient_price } a unit/kg. 
        Quantity remaining is : {self.Ingredient_quantity}
        """
    


class RecipeRequirement(models.Model):
   
   menu_item = models.ForeignKey(MenuItem , on_delete = models.CASCADE)
   ingredient_required = models.ForeignKey(Ingredient , on_delete=models.CASCADE)
   quantity = models.FloatField(default = 0)


   def __str__(self):
    return f"""
    
    menu_item = [{self.menu_item.__str__()}] ;
    ingredient = {self.ingredient_required.Ingredient_name};
    quantity = {self.quantity}
    
    """

    def get_absolute_url(self):
        return ("/menu")
    
    def enough(self):
        return self.quantity <= self.ingredient_required.Ingredient_quantity
    
    def required_cost(self):
        return (self.quantity * self.ingredient_required.Ingredient_price)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem ,on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"""
        You have purchased {self.menu_item} successfully , your date and timestamp is printed below for your records. 
        {self.date_purchased}
        Please note that this receipt is required for returns/refunds!
        """
    
    def get_absolute_url(self):
        return "/purchases"
