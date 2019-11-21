from django.urls import path
from . import views

urlpatterns = [
	path('subject/', views.pro_subject, name='pro_subject'),
	path('coding/',views.pro_coding, name='pro_coding'),
	path('result/',views.pro_result, name = 'pro_result'),
	path('assign/',views.pro_assign, name = 'pro_assign'),
	path('config/',views.pro_config, name = 'pro_config')
]
