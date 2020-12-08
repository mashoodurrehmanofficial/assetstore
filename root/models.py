from django.db import models
from django.db.models.signals import post_save,post_delete,pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver 
import os,uuid,time,random
from datetime import datetime


RAW_SEO_DATA=[
    "unity assets free"
]

class ParentCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        
        
class MainTag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        
class Item(models.Model): 
    title = models.CharField(max_length=200)
    shortname = models.CharField(max_length=200,blank=True)
    version = models.CharField(max_length=200,blank=True)
    latestversion=models.BooleanField(blank=True,default=True)
    filesize = models.CharField(max_length=200,blank=True)
    image = models.FileField(upload_to='files/',blank=True)   
    
    parent = models.ForeignKey(ParentCategory,on_delete=models.CASCADE)
    maintag = models.ForeignKey(MainTag,on_delete=models.CASCADE)
    
    seotags = models.TextField(max_length=1000,blank=True)
    querypurpose = models.ManyToManyField(MainTag,related_name="query")
    intro = models.TextField(max_length=2000,blank=True)
    compatibility = models.TextField(max_length=2000,blank=True)
    reasons = models.TextField(max_length=2000,blank=True)
    P1 = models.TextField(max_length=2000,blank=True)
    P2 = models.TextField(max_length=2000,blank=True)
    P3 = models.TextField(max_length=2000,blank=True)
    features1 = models.TextField(max_length=2000,blank=True)
    features2 = models.TextField(max_length=2000,blank=True)
    more = models.TextField(max_length=2000,blank=True)
    
    storelink = models.CharField(max_length=1000,blank=True)
    fslink = models.CharField(max_length=1000,blank=True)
    
    AUTOSEO = models.BooleanField(default=True);
    insertTOP = models.BooleanField(default=True);
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if self.AUTOSEO is True:
            pass
        
        if 'GB' not in self.filesize:
            self.filesize = self.filesize+" MB"
        if 'MB'  in self.filesize:
            self.filesize = self.filesize 
        if self.shortname =='':
            self.shortname = self.title.replace(' ','-').replace('•','')
        if self.latestversion and '(Latest version)' not in self.version:
            self.version = self.version+" (Latest version)"
        if Item.objects.all().count()!=0: 
            if self.id is not None: pass  
            else:
                self.id = int(time.time())
                itemontop =  Item.objects.all().order_by('-id')[0] 
                if self.insertTOP is False:self.id = Item.objects.all().order_by('id')[0].id-1
        else:self.id = int(time.time())
        super(Item, self).save(*args, **kwargs)
 
    
@receiver(post_save, sender=Item)
def IMAGE_Handling(sender,instance,**kwargs):
    # if instance.insertTOP:
    #     pass
    # else:
        
    
    # os.getcwd()+"\\Media\\files"
    allimage = os.listdir(os.path.join(os.getcwd(),'Media','files')) 
    print("_"*20)
    itemsavedimage = [str(x.image.name).replace('files/','') for x in Item.objects.all()]
    print(itemsavedimage)
    for x in allimage:
        if x in itemsavedimage:
            pass
        elif instance.image.url!='':
            os.remove(os.path.join(os.getcwd(),'Media','files',f'{x}'))
    print("_"*20)
    # Profile.objects.get_or_create(admin=instance)
    pass
    
@receiver(post_delete, sender=Item)
def delete_image(sender, instance, using, **kwargs):
    if instance.image.name: 
        os.remove(os.path.join(os.getcwd(),'Media',f'{instance.image.name}'))
 


class TEST(models.Model): 
    name = models.CharField(max_length=200)
    insertTOP = models.BooleanField(default=True,blank=True);
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if TEST.objects.all().count()!=0: 
            if self.id is not None: pass  
            else:
                self.id = int(time.time())
                itemontop =  TEST.objects.all().order_by('-id')[0] 
                if self.insertTOP is False:self.id = TEST.objects.all().order_by('id')[0].id-1
        else:self.id = int(time.time())
        super(TEST, self).save(*args, **kwargs)
 
        
        
        