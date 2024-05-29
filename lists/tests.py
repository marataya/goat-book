from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest, HttpResponse

from lists.views import home_page
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


