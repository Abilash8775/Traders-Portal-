from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50)
    scripcode = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.company_name

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.company.company_name}"
