from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    location = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/menu/categories', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_picture(self):
        pic = self.picture
        if not pic:
            return '/static/images/coffe_glass.webp'
        return pic.url

    def get_items(self):
        return self.menuitem_set.all()


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=30, decimal_places=0)
    picture = models.ImageField(upload_to='images/menu/items', null=True, blank=True)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_picture(self):
        pic = self.picture
        if not pic:
            return '/static/images/coffe_glass.webp'
        return pic.url
