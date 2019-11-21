# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, BadHeaderError 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from judge.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from judge.models import *
from django.views.generic.base import TemplateView

# Create your views here.

#-- professor
class ProfessorMainLV(TemplateView):
	template_name = 'judge/professor/professor_main_list.html'

class ProfessorSubjectLV(TemplateView):
	template_name = 'judge/professor/professor_subject_list.html'

class ProfessorCreateView(TemplateView):
	template_name = 'judge/professor/professor_assignment_add.html'

class ProfessorUpdateView(TemplateView):
	template_name = 'judge/professor/professor_assignment_update.html'

class ProfessorDeleteView(TemplateView):
	template_name = 'judge/professor/professor_assignment_delete.html'

class ProfessorSettingsView(TemplateView):
	template_name = 'judge/professor/professor_subject_settings.html'

class ProfessorResultLV(TemplateView):
	template_name = 'judge/professor/professor_result_list.html'

#-- student
class StudentMainLV(ListView):
	queryset = None
	template_name = 'judge/student/student_main_list.html'
	
	def post(self,request,*args,**kwargs):
		form = request.POST
		student_id = form.get('id')
		student_name = form.get('name')
		request.session['student_id'] = student_id
		request.session['student_name'] = student_name

		sql = 'SELECT '
		
		student.objects.raw(sql)

		return render(request, self.template_name, {'subject_list_sql': subject_list_sql})	

class StudentSubjectLV(TemplateView):
	queryset = None

	template_name = 'judge/student/student_subject_list.html'
	paginate_by = None

	def get(self, request, *args, **kwargs):
		if request.session['subject_id']:
			sql = ''

			subject_list_sql = student.objects.raw(sql)

			return render(request, self.template_name, { 'subject_list_sql': subject_list_sql})
		else:
			return HttpResponse('This is wrong way!')

	def post(self, request, *args, **kwargs):
		form = request.POST
		request.session['title'] = form.get('title')
		request.session['classes'] = form.get('classes')
		request.session['subject_id'] = form.get('subject_id')

		sql = ''

		subject_list_sql = student.objects.raw(sql)

		return render(request, self.template_name, { 'subject_list_sql': subject_list_sql})


class StudentAssignment(TemplateView):
	template_name = 'judge/student/student_assignment.html'

def Coding(request):
	if request.method == "POST":
		form = CodingForm(request.POST)

		if form.is_valid():
			code = form.cleaned_data['code']
			lang = form.cleaned_data['lang']

			code = code.encode('utf-8')
			print("your code : ",code)	
			print("your lang : ",lang)

			if lang == 'c':
				f = open("./code/code.c",'w')
			elif lang == 'python':
				f = open("./code/code.py",'w')
			elif lang == 'java':
				f = open("./code/code.java",'w')
			
			f.write(code)
			f.close()

			form = CodingForm()

		return render(request, 'judge/student/student_assignment.html', {'form' : form})
	else:
		form = CodingForm()
		
		return render(request, 'judge/student/student_assignment.html', {'form' : form})



