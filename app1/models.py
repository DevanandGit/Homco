# models.py

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from firebase_admin import firestore

class Product(models.Model):
    product_name = models.CharField(max_length=500, unique=True)
    product_category = models.CharField(max_length=500)
    ingredients_list = models.JSONField(default=list)

    def add_ingredients(self, content, quantity, is_product):
        self.ingredients_list.append({
            'content': content,
            'quantity': quantity,
            'is_product': is_product
        })

    def __str__(self):
        return f"Name: {self.product_name}\nCategory: {self.product_category}\nIngredients: {self.ingredients_list}\n"

@receiver(post_save, sender=Product)
def create_or_update_product_firestore_document(sender, instance, created, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('products').document(str(instance.id))
    doc_ref.set({
        'product_name': instance.product_name,
        'product_category': instance.product_category,
        'ingredients_list': instance.ingredients_list,
    })

@receiver(pre_delete, sender=Product)
def delete_product_firestore_document(sender, instance, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('products').document(str(instance.id))
    doc_ref.delete()

class ManPower(models.Model):
    category_name = models.CharField(max_length=500, unique=True)
    packing = models.JSONField(default=list)

    def add_packing(self, quantity, unit, amount):
        self.packing.append({
            'quantity': quantity,
            'unit': unit,
            'amount': amount
        })

    def __str__(self):
        return f"Category Name: {self.category_name}\nPacking: {self.packing}"

@receiver(post_save, sender=ManPower)
def create_or_update_manpower_firestore_document(sender, instance, created, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('manpower').document(str(instance.id))
    doc_ref.set({
        'category_name': instance.category_name,
        'packing': instance.packing,
    })

@receiver(pre_delete, sender=ManPower)
def delete_manpower_firestore_document(sender, instance, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('manpower').document(str(instance.id))
    doc_ref.delete()

class RawMaterial(models.Model):
    material_name = models.CharField(max_length=500, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=20, default='gm', blank=True)

    def __str__(self):
        return f"Raw Material Name: {self.material_name}\nPrice: {self.price}"

@receiver(post_save, sender=RawMaterial)
def create_or_update_rawmaterial_firestore_document(sender, instance, created, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('raw_materials').document(str(instance.id))
    doc_ref.set({
        'material_name': instance.material_name,
        'price': float(instance.price),
        'unit': instance.unit,
    })

@receiver(pre_delete, sender=RawMaterial)
def delete_rawmaterial_firestore_document(sender, instance, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('raw_materials').document(str(instance.id))
    doc_ref.delete()

class PackingMaterial(models.Model):
    pack_name = models.CharField(max_length=500, unique=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, default='ml', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Packing Material Name: {self.pack_name}\nQuantity: {self.quantity}\nunit: {self.unit}\nprice: {self.price}"

@receiver(post_save, sender=PackingMaterial)
def create_or_update_packingmaterial_firestore_document(sender, instance, created, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('packing_materials').document(str(instance.id))
    doc_ref.set({
        'pack_name': instance.pack_name,
        'quantity': instance.quantity,
        'unit': instance.unit,
        'price': float(instance.price),
    })

@receiver(pre_delete, sender=PackingMaterial)
def delete_packingmaterial_firestore_document(sender, instance, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('packing_materials').document(str(instance.id))
    doc_ref.delete()

class Energycost(models.Model):
    category_name = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

@receiver(post_save, sender=Energycost)
def create_or_update_energycost_firestore_document(sender, instance, created, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('energy_costs').document(str(instance.id))
    doc_ref.set({
        'category_name': instance.category_name,
        'cost': float(instance.cost),
    })

@receiver(pre_delete, sender=Energycost)
def delete_energycost_firestore_document(sender, instance, **kwargs):
    db = firestore.client()
    doc_ref = db.collection('energy_costs').document(str(instance.id))
    doc_ref.delete()
