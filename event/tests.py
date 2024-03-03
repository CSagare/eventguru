from django.test import TestCase
from django.urls import reverse
from event.models import Eventplanner, contacts
from event.forms import ContactForm

class EventplannerTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.eventplanner = Eventplanner.objects.create(
            title="Test Eventplanner",
            description="Test Description",
            rating=4.5
            # Add other fields as needed
        )

    def test_index_view(self):
        # Test index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.eventplanner.title)

    def test_contact_form(self):
        # Test contact form submission
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test Message'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Add more test cases as needed
