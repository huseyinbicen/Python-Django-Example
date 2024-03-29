from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
        )
    date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='image/', null = True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title 
