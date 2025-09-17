from django.db import models
from django.contrib.auth.models import User


class WeatherAlert(models.Model):
    """Weather alerts sent to users"""
    
    ALERT_TYPES = [
        ('heavy_rain', 'Heavy Rain'),
        ('drought_warning', 'Drought Warning'),
        ('frost_warning', 'Frost Warning'),
        ('high_wind', 'High Wind'),
        ('heatwave', 'Heatwave'),
        ('cyclone', 'Cyclone'),
        ('hail', 'Hail Storm'),
        ('flood', 'Flood Warning'),
    ]
    
    SEVERITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weather_alerts')
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)
    title = models.CharField(max_length=200)
    message = models.TextField()
    weather_data = models.JSONField(
        help_text="Raw weather data that triggered this alert"
    )
    location_lat = models.DecimalField(max_digits=10, decimal_places=8)
    location_lon = models.DecimalField(max_digits=11, decimal_places=8)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_sent_sms = models.BooleanField(default=False)
    is_sent_email = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.alert_type} ({self.severity})"
    
    class Meta:
        verbose_name = "Weather Alert"
        verbose_name_plural = "Weather Alerts"
        ordering = ['-created_at']


class APIUsageLog(models.Model):
    """Log API usage for monitoring and analytics"""
    
    API_TYPES = [
        ('gemini', 'Gemini AI'),
        ('openweather', 'OpenWeatherMap'),
        ('twilio', 'Twilio SMS'),
    ]
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='api_usage_logs'
    )
    api_type = models.CharField(max_length=20, choices=API_TYPES)
    endpoint = models.CharField(max_length=200)
    request_data = models.JSONField(default=dict, blank=True)
    response_status = models.IntegerField()
    response_time_ms = models.IntegerField(help_text="Response time in milliseconds")
    tokens_used = models.IntegerField(null=True, blank=True, help_text="For AI APIs")
    error_message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.api_type} - {self.response_status} at {self.timestamp}"
    
    class Meta:
        verbose_name = "API Usage Log"
        verbose_name_plural = "API Usage Logs"
        ordering = ['-timestamp']


class SystemConfiguration(models.Model):
    """System-wide configuration settings"""
    
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.key}: {self.value[:50]}..."
    
    class Meta:
        verbose_name = "System Configuration"
        verbose_name_plural = "System Configurations"
