from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from MyBody.catalog.models import Article, LikeArticle, CommentModel
from MyBody.users.models import MyBodyUser


class CatalogTests(TestCase):
    VALID_USER_DATA = {
        'username': 'martin123',
        'email': 'emailTest@abv.bg',
        'password': '123asdQWE@#$%*&^%%$',
    }
    SECOND_USER_DATA = {
        'username': 'user2',
        'email': 'emailTest222@abv.bg',
        'password': '123asdQWE@#$%*&^%%$',
    }

    def __create_user(self, user_data=None):
        if not user_data:
            return MyBodyUser.objects.create_user(**self.VALID_USER_DATA)
        return MyBodyUser.objects.create_user(**user_data)

    @staticmethod
    def __create_image():
        return SimpleUploadedFile(name='test_image.jpg', content=open('media/OIP.jpg', 'rb').read(), content_type='image/jpeg')

    def __create_article(self):
        user = self.__create_user()
        image = self.__create_image()
        article = Article(
            title='Test',
            description='Test Description',
            type='Nutrition',
            image=image,
            owner=user,
        )
        article.save()
        return article

    def test_catalog_template(self):
        response = self.client.get(reverse('catalog'))

        self.assertTemplateUsed(response, 'catalog.html')

    def test_search_template(self):
        response = self.client.get(reverse('search catalog'))

        self.assertTemplateUsed(response, 'search_catalog.html')

    def test_article_create(self):
        article = self.__create_article()
        self.assertEqual(article, Article.objects.first())

    def test_article_details_template(self):
        article = self.__create_article()
        response = self.client.get(reverse('details article', kwargs={'pk': article.id}))
        self.assertTemplateUsed(response, 'details_article.html')

    def test_right_owner_to_article(self):
        article = self.__create_article()
        user = self.__create_user(self.SECOND_USER_DATA)
        self.assertNotEqual(user, article.owner)

    def test_article_likes_increase(self):
        article = self.__create_article()
        like = LikeArticle(
            article=article,
            user=article.owner,
        )
        like.save()
        self.assertEqual(1, article.likearticle_set.count())

    def test_article_comment_create(self):
        article = self.__create_article()
        comment = CommentModel(
            owner=article.owner,
            article=article,
            content='Test Comment',
        )
        comment.save()
        self.assertEqual(1, article.commentmodel_set.count())

    def test_delete_comment_with_owner_user_and_has_permissions(self):
        article = self.__create_article()
        comment = comment = CommentModel(
            owner=article.owner,
            article=article,
            content='Test Comment',
        )
        # Create Group
        group_name = "Regular User"
        group = Group(name=group_name)
        group.save()
        # Add User To Group
        group.user_set.add(article.owner)
        # Login User Creator
        self.client.login(**{'username': 'martin123', 'password': "123asdQWE@#$%*&^%%$"})
        comment.save()
        self.client.get(
            reverse('delete comment', kwargs={'pk': comment.id})
        )
        self.assertEqual(0, article.commentmodel_set.count())

    def test_delete_comment_with_user_who_is_not_owner(self):
        article = self.__create_article()
        comment = comment = CommentModel(
            owner=article.owner,
            article=article,
            content='Test Comment',
        )
        comment.save()
        user2 = self.__create_user(self.SECOND_USER_DATA)
        self.client.login(**{'username': 'user2', 'password': "123asdQWE@#$%*&^%%$"})
        self.client.get(
            reverse('delete comment', kwargs={'pk': comment.id})
        )
        self.assertEqual(1, article.commentmodel_set.count())

    def test_unauthorized_view(self):
        article = self.__create_article()
        comment = comment = CommentModel(
            owner=article.owner,
            article=article,
            content='Test Comment',
        )
        comment.save()
        user2 = self.__create_user(self.SECOND_USER_DATA)
        self.client.login(**{'username': 'user2', 'password': "123asdQWE@#$%*&^%%$"})
        response = self.client.get(
            reverse('delete comment', kwargs={'pk': comment.id})
        )
        self.assertTemplateUsed(response, 'unauthorized_user.html')

    def test_edit_article(self):
        article = self.__create_article()
        group_name = "Regular User"
        group = Group(name=group_name)
        group.save()
        # Add User To Group
        group.user_set.add(article.owner)
        # Login User Creator
        self.client.login(**{'username': 'martin123', 'password': "123asdQWE@#$%*&^%%$"})
        image = self.__create_image()
        self.client.post(
            reverse('edit article', kwargs={'pk': article.id}),
            data={
                'title': 'Changed',
                'description': 'Test Description',
                'type': 'nutrition',
                'image': image,
            }
        )
        self.assertEqual('Changed', Article.objects.first().title)