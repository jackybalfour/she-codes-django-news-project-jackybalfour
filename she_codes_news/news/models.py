from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=25)
    def __str__(self):
        return self.category_name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = 'posts'
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(default="https://picsum.photos/600")
    newsCategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
