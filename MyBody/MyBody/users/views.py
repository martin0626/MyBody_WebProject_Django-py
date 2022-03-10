from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


from MyBody.catalog.models import Article, LikeArticle
from MyBody.users.forms import ProfileForm, RegisterForm, LoginForm
from MyBody.users.helpers import send_email_message
from MyBody.users.models import MyBodyUser, Profile


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'profile_views/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserRegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'profile_views/register_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class UserLogoutView(LogoutView):
    pass


def profile_edit(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details', profile.pk)
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, 'profile_views/profile_create.html', context)


def profile_details(request, pk):

    profile = Profile.objects.get(pk=pk)
    is_owner = request.user and request.user.id == profile.user_id
    user = MyBodyUser.objects.get(pk=pk)
    articles = Article.objects.filter(owner__profile=profile)
    likes = len(list(LikeArticle.objects.filter(article_id__in=articles)))
    context = {
        'user': user,
        'profile': profile,
        'articles': articles,
        'likes': likes,
        'is_owner': is_owner,
    }

    return render(request, 'profile_views/profile_details.html', context)


@login_required(login_url='login/')
def profile_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'profile_views/delete_profile.html')
