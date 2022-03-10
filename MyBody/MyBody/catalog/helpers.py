from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from MyBody.catalog.models import Article, CommentModel


def article_permissions_required(required_permissions):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            pk = kwargs['pk']

            article = Article.objects.get(pk=pk)
            if not user.is_authenticated or not user.has_perms(required_permissions) or not article.owner.id == user.id:
                return redirect('unauthorized view')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


def comments_permissions_required(required_permissions):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            comment = CommentModel.objects.get(pk=kwargs['pk'])
            if not user.is_authenticated or not user.has_perms(required_permissions) or not user.id == comment.owner.id:
                return render(request, 'unauthorized_user.html')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


def add_user_to_default_group(user):
    group = Group.objects.get(name='Regular User')
    group.user_set.add(user)
    return
