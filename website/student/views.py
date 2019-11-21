from django.shortcuts import render
from django.http import HttpResponse

def st_homework(request):
	return render(request,'student/st_homework.html',{})

def st_subject(request):
	return render(request,'student/st_subject.html',{})

#def st_login(request):
#	return render(request,'student/login.html',{})
