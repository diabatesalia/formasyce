from django.db import models

# Create your models here.
class Commande(models.Model):
    STATUS=(('en instance', 'en instance'),
            ('nom livré', 'nom livré'),
            ('livré', 'livré'))
    #client=
    #produit=
    status=models.CharField(max_length=200, null=True, choices=STATUS)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)