from django import forms

class CodingForm(forms.Form):
	code = forms.CharField(widget=forms.Textarea())

	CHOICES = (('python','python'),('c','c'),('java','java'))
	lang = forms.ChoiceField(choices=CHOICES)
