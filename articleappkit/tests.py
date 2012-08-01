from django.test import TestCase


class articleappkitTest(TestCase):
    """
    Tests for django-articleappkit
    """
    def test_articleappkit(self):
        config1 = {'UNIQUE_TOGETHER': ('slug', 'create_date')}
        from articleappkit.models import get_articlebase
        ArticleBase1 = get_articlebase(config1)
        self.assertEqual(ArticleBase1._meta.unique_together, (('slug', 'create_date'), ))

    def test_articleappkit2(self):
        config2 = {'UNIQUE_TOGETHER': ('slug', 'update_date')}
        from articleappkit.models import get_articlebase
        ArticleBase1 = get_articlebase(config2)
        self.assertEqual(ArticleBase1._meta.unique_together, (('slug', 'update_date'), ))
