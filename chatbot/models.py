from django.db import models
from django.contrib.auth.models import User
# For PostgreSQL-specific features (commented for SQLite development)
# from django.contrib.postgres.search import SearchVectorField
# from django.contrib.postgres.indexes import GinIndex


class KnowledgeArticle(models.Model):
    """Knowledge base articles for the RAG chatbot system"""
    
    CATEGORY_CHOICES = [
        ('crop_cultivation', 'Crop Cultivation'),
        ('pest_management', 'Pest Management'),
        ('soil_health', 'Soil Health'),
        ('irrigation', 'Irrigation'),
        ('fertilizers', 'Fertilizers'),
        ('weather_management', 'Weather Management'),
        ('post_harvest', 'Post Harvest'),
        ('marketing', 'Marketing'),
        ('government_schemes', 'Government Schemes'),
        ('organic_farming', 'Organic Farming'),
        ('livestock', 'Livestock'),
        ('general', 'General'),
    ]
    
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('ml', 'Malayalam'),
    ]
    
    title = models.CharField(
        max_length=200, 
        help_text="Title of the knowledge article"
    )
    content = models.TextField(
        help_text="Main content of the article"
    )
    summary = models.TextField(
        blank=True, 
        null=True,
        help_text="Brief summary of the article"
    )
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES,
        help_text="Category of the knowledge article"
    )
    language = models.CharField(
        max_length=5, 
        choices=LANGUAGE_CHOICES,
        default='en',
        help_text="Language of the article"
    )
    tags = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        help_text="Comma-separated tags for better searchability"
    )
    source = models.CharField(
        max_length=200, 
        blank=True, 
        null=True,
        help_text="Source or reference of the information"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this article should be included in searches"
    )
    # search_vector = SearchVectorField(null=True, blank=True)  # PostgreSQL-specific
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} ({self.language})"
    
    class Meta:
        verbose_name = "Knowledge Article"
        verbose_name_plural = "Knowledge Articles"
        indexes = [
            models.Index(fields=['category', 'language']),
            models.Index(fields=['is_active', 'language']),
            # GinIndex(fields=['search_vector']),  # PostgreSQL-specific
        ]


class ChatSession(models.Model):
    """Chat sessions to track user conversations"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sessions')
    session_id = models.CharField(max_length=100, unique=True)
    language = models.CharField(
        max_length=5, 
        choices=KnowledgeArticle.LANGUAGE_CHOICES,
        default='en'
    )
    started_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - Session {self.session_id}"
    
    class Meta:
        verbose_name = "Chat Session"
        verbose_name_plural = "Chat Sessions"
        ordering = ['-last_activity']


class ChatMessage(models.Model):
    """Individual chat messages in a session"""
    
    MESSAGE_TYPES = [
        ('user', 'User Message'),
        ('bot', 'Bot Response'),
        ('system', 'System Message'),
    ]
    
    session = models.ForeignKey(
        ChatSession, 
        on_delete=models.CASCADE, 
        related_name='messages'
    )
    message_type = models.CharField(
        max_length=10, 
        choices=MESSAGE_TYPES
    )
    content = models.TextField(help_text="Message content")
    context_articles = models.ManyToManyField(
        KnowledgeArticle, 
        blank=True,
        help_text="Knowledge articles used as context for this response"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.session.user.username} - {self.message_type} at {self.timestamp}"
    
    class Meta:
        verbose_name = "Chat Message"
        verbose_name_plural = "Chat Messages"
        ordering = ['timestamp']
