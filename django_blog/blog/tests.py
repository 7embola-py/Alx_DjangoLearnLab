from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Tag

class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test Comment'
        )

    def test_post_detail_view(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Comment')

    def test_add_comment(self):
        response = self.client.post(reverse('comment-create', kwargs={'pk': self.post.pk}), {
            'content': 'New Comment'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertTrue(Comment.objects.filter(content='New Comment').exists())

    def test_comment_update(self):
        response = self.client.post(reverse('comment-update', kwargs={'pk': self.comment.pk}), {
            'content': 'Updated Comment'
        })
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Comment')

    def test_comment_delete(self):
        response = self.client.post(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

class TagSearchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        
    def test_create_post_with_tags(self):
        response = self.client.post(reverse('post-create'), {
            'title': 'Tagged Post',
            'content': 'Content',
            'tags': 'django, python'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Tagged Post').exists())
        post = Post.objects.get(title='Tagged Post')
        self.assertEqual(post.tags.count(), 2)
        self.assertTrue(post.tags.filter(name='django').exists())

    def test_search_posts(self):
        post = Post.objects.create(title='Searchable Post', content='Content', author=self.user)
        response = self.client.get(reverse('search'), {'q': 'Searchable'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Searchable Post')

    def test_filter_by_tag(self):
        tag = Tag.objects.create(name='testtag')
        post = Post.objects.create(title='Tagged Post', content='Content', author=self.user)
        post.tags.add(tag)
        
        response = self.client.get(reverse('tags-posts', kwargs={'tag_name': 'testtag'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tagged Post')
