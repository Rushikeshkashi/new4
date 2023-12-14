from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def index(request):
    template = loader.get_template("index.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def corpataeparking(request):
    template = loader.get_template("corpataeparking.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

# def guided(request):
#     template = loader.get_template("guided.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def paypark(request):
#     template = loader.get_template("paypark.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def qrbased(request):
#     template = loader.get_template("qrbased.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def uhf(request):
#     template = loader.get_template("uhf.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))



# def commercial(request):
#     template = loader.get_template("commercial.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))
    
# def residential(request):
#     template = loader.get_template("residential.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def public(request):
#     template = loader.get_template("public.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def pplmanagement(request):
#     template = loader.get_template("pplmanagement.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def builderdeveloper(request):
#     template = loader.get_template("builderdeveloper.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def termcondion(request):
#     template = loader.get_template("termcondion.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def refundpolicy(request):
#     template = loader.get_template("refundpolicy.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def cancaltionpolicy(request):
#     template = loader.get_template("cancaltionpolicy.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))

# def privacypolicy(request):
#     template = loader.get_template("privacypolicy.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))