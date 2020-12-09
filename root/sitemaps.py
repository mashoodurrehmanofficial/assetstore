from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from datetime import datetime
from .models import Item,ParentCategory,MainTag

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'


    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class Article_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Item.objects.all()

    def location(self, obj):
        return '/'+obj.url

    def lastmod(self, obj): 
        return datetime.today()