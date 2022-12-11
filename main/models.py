from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self) -> str:
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_categories")

    class Meta:
        verbose_name_plural = "sub Categories"
    def __str__(self) -> str:
        return self.title

class Author(models.Model):
    avatar = models.ImageField(upload_to="author/images")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"  

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="blogs")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name="blogs")
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover= models.ImageField(upload_to="cover/images")

    def __str__(self) -> str:
        return self.title