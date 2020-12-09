from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from .models import *


# Create your views here.
# INDEX PAGE
def index(request): 
    items = Item.objects.all()
    context = {
        'title':'Unity paid assets for free | Unity free paid assets | Download unity paid assets for free ',
        "items":items
    }
    return render(request, "root/index.html",context)


def itempage(request,grabItem):
    print('______',grabItem)
    if 'favicon.ico' in grabItem:
        return redirect('/')
    else:
        requiredItem = Item.objects.filter(url=grabItem).first()
        allitems = Item.objects.all().exclude(id=requiredItem.id) 
        rightbaritems = allitems[:4] if allitems.count() >=4 else allitems
        bottom1 = allitems[4:7] if allitems.count() >=7 else allitems
        RAW_SEO=['** free download','unity ** free download ']
        RAW_SEO=[x.replace('**',requiredItem.heading.replace(' - free download','')) for x in RAW_SEO]
        context={
            "miniseo":' '.join(RAW_SEO),
            "heading":requiredItem.heading,
            "title":requiredItem.title,
            "url":requiredItem.url,
            "image":requiredItem.image,
            "version":requiredItem.version,
            "islatestversion":requiredItem.latestversion,
            "filesize":requiredItem.filesize,
            "parent":requiredItem.parent.name,
            "maintag":requiredItem.maintag.name,
            "assetstorelink":requiredItem.assetstorelink,
            "intro":requiredItem.intro,
            "description":requiredItem.description,
            "seotags":requiredItem.seotags,
            "compatibility":requiredItem.compatibility.split('●'),
            "features1":requiredItem.features1.split('●'),
            "more":requiredItem.more.split('●'), 
            'rightbaritems':rightbaritems,
            'bottom1':bottom1,
            
        }
        return render(request, "root/itempage.html",context)
 

def grabparentcategory(request,category):
    items = Item.objects.filter(parent__name=category)
    context = {
        'title':f'{category} '+'Unity paid assets for free | Unity free paid assets | Download unity paid assets for free ',
        "items":items
    }
    return render(request, "root/index.html",context)
 
 
 
def grabmainTagCategory(request,parent,maintag): 
    items = Item.objects.filter(parent__name=parent,maintag__name=maintag)
    context = {
        'title':f'{parent} | {maintag} | '+'Unity paid assets for free | Unity free paid assets | Download unity paid assets for free ',
        "items":items
    }
    return render(request, "root/index.html",context)
 
 
def search(request): 
    if request.method == 'GET': 
        query = request.GET['query']
        
        
        set1 = Item.objects.filter(parent__name__icontains=query) 
        set2 = Item.objects.filter(maintag__name__icontains=query) 
        set3 = Item.objects.filter(title__icontains=query) 
        set4 = Item.objects.filter(seotags__icontains=query) 
        # set2 = Snippets.objects.filter(heading__contains=query) 
        context={
            'query': query,
            'items': set1.union(set2,set3,set4)
        }
        return render(request, "root/index.html",context)
 
 
 
 
def adminfucs(request):
    return render(request, "root/admin.html")
 
def autocom(request):
    text = request.GET['value']
    results =[x.title for x in  Item.objects.filter(title__icontains=text)]
    return JsonResponse({"results":results})
 