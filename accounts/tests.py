from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class AccountModelTestCase(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="john@gmail.com",
            password="abcd1234",
        )
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.username, "johndoe")
        self.assertEqual(user.email, "john@gmail.com")
        self.assertTrue(user.check_password("abcd1234"))

        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superadmin)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            first_name="Obaidur",
            last_name="Rahman",
            username="obaidur",
            email="obaidur@gmail.com",
            password="abcdabcd",
        )
        self.assertEqual(user.first_name, "Obaidur")
        self.assertEqual(user.last_name, "Rahman")
        self.assertEqual(user.username, "obaidur")
        self.assertEqual(user.email, "obaidur@gmail.com")
        self.assertTrue(user.check_password("abcdabcd"))

        self.assertTrue(user.is_admin)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superadmin)
        self.assertTrue(user.is_active)
