from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout as user_logout, login as user_login
from django.contrib.auth.decorators import login_required


from .forms import RegistrationForm, LoginForm
from . import models


"""
Mixins
"""
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


"""
Account Views
"""
class AccountView(LoginRequiredMixin, generic.DetailView):

    model = models.Brother
    template_name = 'account/account.html'

    def get(self, request, *args, **kwargs):
        """Load the member"""
        return get_object_or_404(models.Brother, slug=self.request.user.username)


class UpdateAccountView(LoginRequiredMixin, generic.UpdateView):

    model = models.Brother
    template_name = 'account/update.html'
    success_url = '/account/'
    fields = ['user', 'chapter']

    def get_object(self):
        """Load the brother"""
        return get_object_or_404(models.Brother, slug=self.request.user.username)


class RegisterView(generic.FormView):

    template_name = 'account/register.html'
    form_class = RegistrationForm
    success_url = '/account/'

    def form_valid(self, form):
        """Register the user if the form is valid."""
        form.register_member(self.request)
        return super(RegisterView, self).form_valid(form)


class LoginView(generic.FormView):

    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = '/profile/'

    def form_valid(self, form):
        form.login_brother(self.request)
        return super(LoginView, self).form_valid(form)


def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')

"""
Profile Views
"""
class ProfileView(generic.DetailView):

    model = models.Brother
    template_name = 'profile/profile.html'

    def get_object(self):
        """Load the brother"""
        username = self.request.user.username
        try:
            return models.Brother.objects.get(slug=username)
        except models.Brother.DoesNotExist:
            return HttpResponseRedirect('/profile/%s' % username)


class GroupsView(generic.DetailView):

    model = models.Group
    template_name = 'group/group.html'


"""
Group Views
"""
class GroupView(generic.DetailView):

    model = models.Group
    template_name = 'group/group.html'


class CreateGroupView(generic.CreateView):

    model = models.Group
    template_name = 'group/group.html'