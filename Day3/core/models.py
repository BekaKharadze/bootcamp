from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)   


class Product(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.post.title}"