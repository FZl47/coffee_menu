from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=30, decimal_places=0)
    picture = models.ImageField(upload_to='images/menu/items', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_picture(self):
        pic = self.picture
        if not pic:
            return '/static/images/coffe_glass.webp'
        return pic.url
