from django.shortcuts import render

def pro_subject(request):
	return render(request,'professor/pro_main.html')

def pro_coding(request):
	return render(request,'professor/pro_management.html')

def pro_result(request):
	return render(request,'professor/pro_results.html')

def pro_assign(request):
	return render(request,'professor/pro_assign.html')

def pro_config(request):
	return render(request,'professor/pro_config.html')

