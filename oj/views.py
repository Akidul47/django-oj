from django.shortcuts import render

from django.views.generic.edit import FormView
from .forms import CompilerModelForm

class IndexView(FormView):
    template_name = "oj/index.html"
    form_class = CompilerModelForm
    success_url = '/thanks/'


