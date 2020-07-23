from django.db import models

class Policy(models.Model):
    policy_choices=(
        ("Motor Insurance","Motor Insurance"),
        ("Other","Other")
    )
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.EmailField(max_length = 254)
    Insurance_type=models.CharField(choices=policy_choices,max_length=16)
    Address=models.CharField(max_length=200)
    Phone=models.CharField(max_length=10)

    def __str__(self):
        return self.Email

class Insurance(models.Model):
    Email = models.EmailField(max_length = 254)
    Price=models.CharField(max_length=100)
    Estimated_amount=models.CharField(max_length=100)

    def __str__(self):
        return self.Email
    