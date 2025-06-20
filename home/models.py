from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Categories(models.Model):
    name= models.CharField(max_length=50, unique=True,validators=[MinLengthValidator(2,message="Category name must be at least 2 characters long.")])

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ISBN(models.Model):
    author_title= models.CharField(max_length=255)
    book_title= models.CharField(max_length=255)
    book = models.OneToOneField('Books', on_delete=models.CASCADE, primary_key=True, related_name='isbn_details' 
    )


class Books(models.Model):
    title = models.CharField('Book Title', max_length=255, validators=[
            MinLengthValidator(10, message="Book title must be at least 10 characters long."),
            MaxLengthValidator(50, message="Book title cannot exceed 50 characters.")
        ])
    description = models.TextField("Description")
    rate = models.PositiveBigIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)

    # isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Books"

    def __str__ (self):
        return self.title
