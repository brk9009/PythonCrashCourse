from django.db import models

class Pizza(models.Model):
    """Types of pizzas"""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        if(len(self.text) > 50):
            return self.text[:50] + "..."
        else:
            return self.text
        
class Toppings(models.Model):
    """Choice of Toppings"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    
    def __str__(self):
        if(len(self.text) > 50):
            return self.text[:50] + "..."
        else:
            return self.text
