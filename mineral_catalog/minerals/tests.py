from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral


class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Kryptonite"
        )
        self.assertEqual(mineral.name, "Kryptonite")


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name="Kryptonite",
            image_caption="The weakness of Superman",
            category="Fictional"
        )
        self.mineral2 = Mineral.objects.create(
            name="Dilithium",
            image_caption="The favorite mineral of Scotty the Engineer",
            category="Fictional"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/list.html')
        self.assertContains(resp, self.mineral1.name)
        self.assertContains(resp, self.mineral2.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral2.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral2, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral2.name)
        self.assertContains(resp, self.mineral2.image_caption)
        self.assertContains(resp, "Category")
        self.assertContains(resp, self.mineral2.category)
