from django.test import TestCase ,Client
from ..models import Menu
from ..serializers import MenuSerializer
from django.urls import reverse
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=120, inventory=50)
        self.item3 = Menu.objects.create(title="Pasta", price=60, inventory=3)

    def test_getall(self):
        url = reverse('menu')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus , many=True)

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), serializer.data)