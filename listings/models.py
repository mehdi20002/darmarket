from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    PROPERTY_TYPES = [
        ('HOUSE', 'Maison'),
        ('APARTMENT', 'Appartement'),
        ('LAND', 'Terrain'),
        ('COMMERCIAL', 'Local commercial'),
    ]

    TRANSACTION_TYPES = [
        ('SALE', 'Vente'),
        ('RENT', 'Location'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    area = models.DecimalField(max_digits=8, decimal_places=2)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    main_image = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
