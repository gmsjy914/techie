from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def porfile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        from profileapp.models import Profile
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated
