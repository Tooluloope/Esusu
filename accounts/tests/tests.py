from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import UserProfile


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        # profile = UserProfile.objects.create(phone_number='123123123')
        user = User.objects.create_user(username ='aliko', first_name='dangote',last_name = 'aliko', email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is Not None for the AbstractUser option
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='1', password="foo", username='tboy')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('nobodey','super@user.com','somebodey')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.username, 'nobodey')

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username = 'nobodey',email='super@user.com', password='foo', is_superuser=False)
