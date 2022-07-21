from .models import User
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

class UserList(TemplateView):
    template_name = "accounts/users.html"
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = User.objects.all()
        context.update({'users':data})
        return context
