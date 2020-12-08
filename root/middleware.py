# from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
# def open_access_middleware(get_response):
#     def middleware(request): 
#         response = get_response(request)
#         response["Access-Control-Allow-Origin"] = "*"
#         response["Access-Control-Allow-Headers"] = "*"
#         return response
#     return middleware

# import uuid
# from root.models import *
# def underdevelop(get_response):
#     def middleware(request):
#         UNDERCONS = StateManager.objects.get(name='undercons')
#         if UNDERCONS.state:
#             print(request.path)
#             if request.path.startswith('/admin/'):
#                 pass
#             elif request.path.startswith('/undercons/'):
#                 UNDERCONS.state= not UNDERCONS.state
#                 UNDERCONS.save()
#             elif not request.path.startswith('/admin/'):
#                 return render(request, 'root/undercons.html')
         
#         else:pass
        
#         response = get_response(request)
#         response["Access-Control-Allow-Origin"] = "*"
#         response["Access-Control-Allow-Headers"] = "*"
#         return response
#     return middleware

