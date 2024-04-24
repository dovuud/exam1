from django.db import models
from django.forms import ImageField


# Create your models here.
class TimeStapmedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStapmedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name

class Tag(TimeStapmedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name

class Author(TimeStapmedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image= models.ImageField(upload_to='author_images')

    def __str__(self):
        return self.name

class Post(TimeStapmedModel):
    title = models.CharField(max_length=212)
    body = models.TextField()
    image = models.ImageField(upload_to='post_images')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag =models.ManyToManyField(Tag)

    def __str__(self):
        return self.title