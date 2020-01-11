from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.
class LoginView(generic.TemplateView):
    template_name = 'login/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        text = 'lol'
        if form.is_valid():
            text = form.cleaned_data['post']
            form = LoginForm()
            context = {
                'errors': form.errors,
                'valid': form.is_valid(),
                'text': 'lol',
            }    
        return render(request, self.template_name, context)

# def Login(request):
#     return render(request, 'login/login.html')