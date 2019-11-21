from django.urls import path
from . import views

urlpatterns = [
	path('homework/', views.st_homework),
	path('subject/',views.st_subject, name='st_subject'),
	#path('login/',views.st_login)
]
