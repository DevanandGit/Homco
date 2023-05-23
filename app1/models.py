from django.db import models
from django.core.exceptions import ValidationError

# from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    product_name = models.CharField(max_length = 500, unique=True)
    product_category = models.CharField(max_length = 500)
    ingredients_list = models.JSONField(default=list)
    
    def add_ingredients(self, content, quantity, is_product):
        self.ingredients_list = {"quantity":quantity, "content":content, "is_product": bool(is_product)}

        

    def __str__(self) -> str:
        return f"Name: {self.Product_name}\nCategory: {self.product_category}\nIngredients: {self.ingredients_list}\n"
    
class ManPower(models.Model):
    category_name = models.CharField(max_length=500, unique=True)
    packing = models.JSONField(default=list)

    def add_packing(self, quantity, unit, amount):
        self.packing = {'quantity': int(quantity),'unit': unit,'amount': round(float(amount),2)}
        self.save()
        
    
    def __str__(self) -> str:
        return f"Category Name: {self.category_name}\nPacking: {self.packing}"



class RawMaterial(models.Model):
    material_name = models.CharField(max_length=500, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=20, default='gm', blank=True)

    def __str__(self) -> str:
        return f"Raw Material Name: {self.material_name}\nPrice: {self.price}"
    
class PackingMaterial(models.Model):
    pack_name = models.CharField(max_length=500, unique=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, default='ml', blank=True) #need to clarify
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"Packing Material Name: {self.pack_name}\nQuantity: {self.quantity}\nunit: {self.unit}\nprice: {self.price}"
    
class Energycost(models.Model):
    category_name = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=8, decimal_places=2)


{
    "product_name": "svds",
    "product_category": "rbvev",
    "ingredients_list": [{"quantity":4, "content":"content", "is_product":"True"}]
}