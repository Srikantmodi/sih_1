from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class FarmProfile(models.Model):
    """Farm profile information for each user"""
    
    SOIL_CHOICES = [
        ('clay', 'Clay'),
        ('sandy', 'Sandy'),
        ('loamy', 'Loamy'),
        ('silt', 'Silt'),
        ('peaty', 'Peaty'),
        ('chalky', 'Chalky'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location_lat = models.DecimalField(
        max_digits=10, 
        decimal_places=8,
        validators=[
            MinValueValidator(-90.0),
            MaxValueValidator(90.0)
        ],
        help_text="Latitude coordinate of the farm"
    )
    location_lon = models.DecimalField(
        max_digits=11, 
        decimal_places=8,
        validators=[
            MinValueValidator(-180.0),
            MaxValueValidator(180.0)
        ],
        help_text="Longitude coordinate of the farm"
    )
    farm_size = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Farm size in acres"
    )
    primary_crops = models.CharField(
        max_length=200, 
        help_text="Comma-separated list of primary crops"
    )
    soil_type = models.CharField(
        max_length=50, 
        choices=SOIL_CHOICES,
        help_text="Primary soil type of the farm"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Farm - {self.farm_size} acres"
    
    class Meta:
        verbose_name = "Farm Profile"
        verbose_name_plural = "Farm Profiles"


class DiaryEntry(models.Model):
    """Farm diary entries for tracking daily activities"""
    
    ACTIVITY_CHOICES = [
        ('sowing', 'Sowing'),
        ('fertilizing', 'Fertilizing'),
        ('watering', 'Watering'),
        ('harvesting', 'Harvesting'),
        ('pest_control', 'Pest Control'),
        ('weeding', 'Weeding'),
        ('pruning', 'Pruning'),
        ('irrigation', 'Irrigation'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_entries')
    date = models.DateField(help_text="Date of the activity")
    activity_type = models.CharField(
        max_length=20, 
        choices=ACTIVITY_CHOICES,
        help_text="Type of farming activity"
    )
    notes = models.TextField(help_text="Detailed notes about the activity")
    crop_involved = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Specific crop involved in this activity"
    )
    area_covered = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(0.01)],
        help_text="Area covered in acres (optional)"
    )
    weather_condition = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Weather condition during activity"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"
    
    class Meta:
        verbose_name = "Diary Entry"
        verbose_name_plural = "Diary Entries"
        ordering = ['-date', '-created_at']
