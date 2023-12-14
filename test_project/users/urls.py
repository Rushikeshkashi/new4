from django.urls import path
from . import views


urlpatterns = [


    path('', views.index, name='index'),
    # path('guided', views.guided, name='guided.html'),
    # path('paypark', views.paypark, name='paypark.html'),
    # path('uhf', views.uhf, name='uhf.html'),
    # path('qrbased', views.qrbased, name='qrbased.html'),
    path('corpataeparking', views.corpataeparking, name='corpataeparking.html'),
    # path('commercial', views.commercial, name='commercial.html'),
    # path('residential', views.residential, name='residential.html'),
    # path('public', views.public, name='public.html'),
    # path('pplmanagement', views.pplmanagement, name='pplmanagement.html'),
    # path('builderdeveloper', views.builderdeveloper, name='builderdeveloper.html'),
    # path('termcondion', views.termcondion, name='termcondion.html'),
    # path('refundpolicy', views.refundpolicy, name='refundpolicy.html'),
    # path('cancaltionpolicy', views.cancaltionpolicy, name='cancaltionpolicy.html'),
    # path('privacypolicy', views.privacypolicy, name='privacypolicy.html'),
    
   
]