from django.shortcuts import render
from django.views.generic import CreateView

from profileapp.forms import ProfileForm
from profileapp.models import Profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profileapp/create.html'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('accountapp:detail',
                       kwargs={'pk': self.kwargs['pk']})
