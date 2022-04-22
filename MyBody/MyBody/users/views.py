from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView

from MyBody.catalog.models import Article, LikeArticle

from MyBody.users.forms import ProfileForm, RegisterForm, LoginForm, ChangePassword

from MyBody.users.models import Profile, MyBodyUser


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'profile_views/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        self.request.session['viewed_articles_ids'] = []
        return result


class UserRegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'profile_views/register_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        self.request.session['viewed_articles_ids'] = []
        return result


class UserLogoutView(LogoutView):
    pass


class ChangePasswordView(PasswordChangeView):
    template_name = 'profile_views/change_password.html'
    form_class = ChangePassword


class ProfileEdit(UpdateView):
    template_name = 'profile_views/profile_create.html'
    form_class = ProfileForm
    model = Profile

    def dispatch(self, request, *args, **kwargs):
        if kwargs['pk'] != request.user.id:
            return redirect('unauthorized view')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


class ProfileDetails(TemplateView):
    template_name = 'profile_views/profile_details.html'
    model = Profile

    def get_context_data(self, **kwargs):
        user = self.request.user
        articles = Article.objects.filter(owner_id=self.request.user.id)
        likes = len(list(LikeArticle.objects.filter(article_id__in=articles)))
        is_owner = self.request.user and self.request.user.id == self.request.user.id
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'profile': self.request.user.profile,
                'user': user,
                'articles': articles,
                'likes': likes,
                'is_owner': is_owner,
            }
        )
        return context


@login_required(login_url='login/')
def profile_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'profile_views/delete_profile.html')
