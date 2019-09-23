from django.db import models

# Create your models here.
class Hotels(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    available_date = models.DateTimeField()
    Hotel_name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.BooleanField(default=False)

    def get_available_date(self):
        return self.available_date

    def get_discount(self):
        return self.discount

    def __str__(self):
        return self.Hotel_name

