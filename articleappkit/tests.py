from django.test import TestCase


class articleappkitTest(TestCase):
    """
    Tests for django-articleappkit
    """
    def test_articleappkit(self):
        config1 = {'UNIQUE_TOGETHER': ('slug', 'create_date')}
        from articleappkit.models import get_article_base
        ArticleBase1 = get_article_base(config1)
        self.assertEqual(ArticleBase1._meta.unique_together, (('slug', 'create_date'), ))

    def test_articleappkit2(self):
        config2 = {'UNIQUE_TOGETHER': ('slug', 'update_date')}
        from articleappkit.models import get_article_base
        ArticleBase1 = get_article_base(config2)
        self.assertEqual(ArticleBase1._meta.unique_together, (('slug', 'update_date'), ))
