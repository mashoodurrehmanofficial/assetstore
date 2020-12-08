
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
    path('', index, name='index'),    
    path('<str:grabItem>/', itempage, name='itempage'),    
    path('category/<str:category>/', grabparentcategory, name='grabparentcategory'),    
    path('category/<str:parent>/<str:maintag>/', grabmainTagCategory, name='grabmainTagCategory'),    
    path('search', search, name='search'),    
    # path('<str:grabItem>/', itempage, name='itempage'),    
    path('admin/admin/admin/adminfucs/', adminfucs, name='adminfucs'),    
    path('admin/admin/admin/autocom/', autocom, name='autocom'),    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

