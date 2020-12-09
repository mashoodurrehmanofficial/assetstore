from django.db import models
from django.db.models.signals import post_save,post_delete,pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver 
from PIL import Image
from bs4 import BeautifulSoup


import os,uuid,time,random,requests
from datetime import datetime


RAW_SEO_DATA=[
    "unity assets for free","unity assets free download",'unity paid assets for free',"unity free paid assets",
    '** free download','unity *** free download','** latest version free download','** latest version download'
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
    assetstorelink = models.CharField(max_length=1000,blank=True)
    fslink = models.CharField(max_length=1000,blank=True) 
    AUTOGENRATE=models.BooleanField(blank=True,default=False)
    AUTOSEO = models.BooleanField(default=True);
    insertTOP = models.BooleanField(default=True);
    heading = models.CharField(max_length=200,blank=True)
    title = models.CharField(max_length=200,blank=True)
    url = models.CharField(max_length=200,blank=True)
    version = models.CharField(max_length=200,blank=True)
    support_versions = models.CharField(max_length=200,blank=True)
    latestversion=models.BooleanField(blank=True,default=True)
    filesize = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='files/',blank=True)   
    
    parent = models.ForeignKey(ParentCategory,on_delete=models.CASCADE)
    maintag = models.ForeignKey(MainTag,on_delete=models.CASCADE)
    
    seotags = models.TextField(max_length=1000,blank=True)
    querypurpose = models.ManyToManyField(MainTag,related_name="query")
    description = models.TextField(blank=True)
    intro = models.TextField(max_length=2000,blank=True)
    compatibility = models.TextField(max_length=2000,blank=True)
    reasons = models.TextField(max_length=2000,blank=True)
    P1 = models.TextField(max_length=2000,blank=True)
    P2 = models.TextField(max_length=2000,blank=True)
    P3 = models.TextField(max_length=2000,blank=True)
    features1 = models.TextField(max_length=2000,blank=True)
    features2 = models.TextField(max_length=2000,blank=True)
    more = models.TextField(max_length=2000,blank=True)
    

    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if self.AUTOGENRATE is True and self.assetstorelink !='':
            self.x = requests.get(self.assetstorelink)
            soup = BeautifulSoup(self.x.text,'lxml')
            soupdes = soup.find('div', attrs={'class':'_3MR2i pc'})
            soup = soup.find('div', attrs={'class':'_3ZV2G m3_2T _9EVz3 _2CNUL wnn-Y'})
            self.heading = soup.find('h1').text+' - free download'
            self.title = self.heading+' | unity free paid assets'
            soup = soup.find('div',attrs={'class':'_2nw25'})
            self.filesize = soup.find('div',attrs={'class':'_27124 product-size'}).text.split('File size')[1] 
            self.version = soup.find('div',attrs={'class':'_27124 product-version'}).text.split('Latest version')[1]  
            self.support_versions = soup.find('div',attrs={'class':'_27124 product-support_version'}).text.split('Supported Unity versions')[1]  
            self.url=self.heading.replace('  ',' ').replace(' ','-').replace('--','-').replace('--','-')
        
        
        
        
        else:
            if self.title.endswith(' '):
                self.title.replace(' ','')
            if 'GB' not in self.filesize and 'MB' not in self.filesize:
                self.filesize = self.filesize+" MB"
            if 'MB'  in self.filesize:
                self.filesize = self.filesize 
            if self.url =='':
                self.url = self.title.replace(' ','-').replace('•','')+'-free-download'
            if ' - free download' not in self.title:
                self.title = self.title+' - free download' 
            if '-free-download' not in self.url:
                self.url = self.url+'-free-download' 
            if self.latestversion and '(Latest version)' not in self.version:
                self.version = self.version+" (Latest version)"    
                
        if self.AUTOSEO is True:
            self.seotags = [str(x).replace('**', self.heading.replace(' - free download','')) for x in RAW_SEO_DATA]
            self.seotags = ' , '.join(self.seotags)
            

        if Item.objects.all().count()!=0: 
            if self.id is not None: pass  
            else:
                self.id = int(time.time())
                itemontop =  Item.objects.all().order_by('-id')[0] 
                if self.insertTOP is False:self.id = Item.objects.all().order_by('id')[0].id-1
        else:self.id = int(time.time())  
        self.AUTOGENRATE=False
        super(Item, self).save(*args, **kwargs)
        imag = Image.open(self.image.path)
        if imag.width > 400 or imag.height> 300:
            output_size = (400, 300)
            imag.thumbnail(output_size)
            imag.save(self.image.path)
 
    
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
 
        
        
        