from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
class RegisterView(generic.CreateView):
    template_name = 'users/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)