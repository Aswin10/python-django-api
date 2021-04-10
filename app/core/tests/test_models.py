from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """TEST Creating user with email is successful"""
        email = 'test@gmail.com'
        password = 'test@123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalised(self):
        """TEST Creating user with normalised email"""

        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test@123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_valid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')


    def test_create_new_super_user(self):
        """Test create new super user"""
        user = get_user_model().objects.create_superuser(
            'testsuper@gmail.com',
            'test@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)