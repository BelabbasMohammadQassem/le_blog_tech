from django.db import models


class Category (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class Article(models.Model):
    title = models.CharField(max_length=200)
    contenu_text = models.TextField()
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
