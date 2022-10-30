from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CompilerModelForm

class IndexView(CreateView):
    template_name = "oj/index.html"
    form_class = CompilerModelForm
    success_url = '/thanks/'

    def form_valid(self, form):
        print("form validation: ", self.get_context_data())
        print("is valid: ", form.is_valid())
        return super().form_valid(form)


class SubmitView(TemplateView):
    template_name = "oj/success.html"
