from django.db.models import QuerySet
from django.test import TestCase

from lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertContains(response, "A new list item")
        self.assertTemplateUsed(response, 'home.html')
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new item'
        # response = home_page(request)
        # self.assertIn('A new item', response.content.decode())
        #
        # expected_content = render_to_string('home.html', {'new_item_text': 'A new item'})
        # self.assertEqual(response.content.decode(), expected_content)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items: QuerySet = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")

