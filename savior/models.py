from django.db import models

# Create your models here.

#일본
class Japan_clothes(models.Model):
    japan_clothes = models.CharField(max_length=10)

    def __str__(self):
        return self.japan_clothes

class Japan_foods(models.Model):
    japan_foods = models.CharField(max_length=10)

    def __str__(self):
        return self.japan_foods
    
class Japan_others(models.Model):
    japan_others = models.CharField(max_length=10)

    def __str__(self):
        return self.japan_others

#미국
class USA_clothes(models.Model):
    usa_clothes = models.CharField(max_length=10)

    def __str__(self):
        return self.usa_clothes

class USA_foods(models.Model):
    usa_foods = models.CharField(max_length=10)

    def __str__(self):
        return self.usa_foods
    
class USA_others(models.Model):
    usa_others = models.CharField(max_length=10)

    def __str__(self):
        return self.usa_others
    
#베트남
class Vietnam_clothes(models.Model):
    vietnam_clothes = models.CharField(max_length=10)

    def __str__(self):
        return self.vietnam_clothes

class Vietnam_foods(models.Model):
    vietnam_foods = models.CharField(max_length=10)

    def __str__(self):
        return self.vietnam_foods
    
class Vietnam_others(models.Model):
    vietnam_others = models.CharField(max_length=10)

    def __str__(self):
        return self.vietnam_others