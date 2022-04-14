from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from MyBody.home.models import ArticleTypes


class HomeViewsTests(TestCase):

    def test_home_view_visualization(self):
        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'index.html')

    def test_details_view_visualization(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=open('media/OIP.jpg', 'rb').read(), content_type='image/jpeg')
        article_detail = ArticleTypes(
            title='Test',
            description='Test Description',
            image=image,
        )
        article_detail.save()
        response = self.client.get(reverse('article info', kwargs={'pk': article_detail.pk}))
        self.assertTemplateUsed(response, 'home_views/article_type_details.html')

    def test_details_creation(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=open('media/OIP.jpg', 'rb').read(), content_type='image/jpeg')
        article_detail = ArticleTypes(
            title='Test',
            description='Test Description',
            image=image,
        )
        article_detail.save()
        self.assertEqual(article_detail, ArticleTypes.objects.first())

    def test_details_delete(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=open('media/OIP.jpg', 'rb').read(), content_type='image/jpeg')
        article_detail = ArticleTypes(
            title='Test',
            description='Test Description',
            image=image,
        )
        article_detail.save()
        article_detail.delete()
        self.assertEqual(None, ArticleTypes.objects.first())