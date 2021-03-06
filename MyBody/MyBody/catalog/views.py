from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from MyBody.catalog.filters import ArticleTypeFilter
from MyBody.catalog.forms import CreateForm, EditForm, DeleteArticleForm, CreateCommentForm
from MyBody.catalog.helpers import article_permissions_required, comments_permissions_required
from MyBody.catalog.models import Article, LikeArticle, CommentModel


class UnauthorizedView(TemplateView):
    template_name = 'unauthorized_user.html'


class SearchView(ListView):
    model = Article
    template_name = 'search_catalog.html'
    ordering = 'title'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleTypeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CatalogView(ListView):
    model = Article
    template_name = 'catalog.html'
    context_object_name = 'articles'
    ordering = ('title',)
    paginate_by = 3


class CreateArticle(LoginRequiredMixin, CreateView):
    model = Article
    form_class = CreateForm
    template_name = 'create_catalog.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('unauthorized view')
        return super().dispatch(request, *args, **kwargs)


@article_permissions_required(required_permissions=['catalog.change_article'])
def edit_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = article.owner
            article.save()
            return redirect('details article', pk)

    else:
        form = EditForm(initial=article.__dict__)

    context = {
        'form': form,
    }
    return render(request, 'edit_catalog.html', context)


@article_permissions_required(required_permissions=['catalog.delete_article'])
def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('catalog')
    else:
        context = {
            'article': article
        }

    return render(request, 'delete_catalog.html', context)


def details_article(request, pk):
    article = Article.objects.get(pk=pk)
    user = request.user
    likes = len(LikeArticle.objects.filter(article_id=pk))
    comments = CommentModel.objects.filter(article_id=pk)

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = user
            comment.article = article
            comment.save()
            return redirect('details article', article.id)

    else:
        viewed_articles_ids = request.session.get('viewed_articles_ids', [])

        viewed_articles_ids.insert(0, pk)
        request.session['viewed_articles_ids'] = viewed_articles_ids[:3]
        form = CreateCommentForm()
    context = {
        'form': form,
        'article': article,
        'likes_count': likes,
        'comments': comments,
    }

    if not user.is_anonymous:
        is_liked = len(list(LikeArticle.objects.filter(article=article, user=user))) > 0
        is_owner = article.owner == user
        context['is_liked'] = is_liked
        context['is_owner'] = is_owner

    return render(request, 'details_article.html', context)


@permission_required('catalog.add_likearticle', 'catalog.delete_likearticle')
def like_article(request, pk):
    article = Article.objects.get(pk=pk)
    user = request.user
    like = LikeArticle.objects.filter(article=article, user=user)

    if not like:
        like = LikeArticle(article_id=article.id, user=user)
        like.save()

    else:
        like.delete()

    return redirect('details article', pk)


@comments_permissions_required(required_permissions=['catalog.delete_commentmodel'])
def delete_comment(request, pk):
    comment = CommentModel.objects.get(pk=pk)
    article_id = comment.article_id
    comment.delete()
    return redirect('details article', article_id)
