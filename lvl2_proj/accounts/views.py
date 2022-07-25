from django.shortcuts import render
from django.core.exceptions import ValidationError
# from .models import User
from django.views.generic import TemplateView, View
from .forms import UserRegistration

# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

class UserSignUp(View):
    # template_name = "accounts/users.html"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     data = User.objects.all()
    #     context.update({'users':data})
    #     return context
    
    def get(self, request):
        form = UserRegistration()
        data = {'form':form}
        return render(request, 'accounts/registration.html', data)
    
    def post(self, request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html')
        raise ValidationError("Invalid Form Data")