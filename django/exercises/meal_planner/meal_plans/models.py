from django.db import models

class Meal(models.Model):
    """Meals for a meal plan"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation"""
        return self.name

class Food(models.Model):
    """Foods for a meal plan"""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'foods'

    def __str__(self):
        """Return a string representation"""
        return self.name