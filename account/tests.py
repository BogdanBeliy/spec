from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate


class AuthTest(APITestCase):

    def setUp(self) -> None:
        url = 'http://127.0.0.1:8000/api/v1/account/auth/'
        self.create_user = self.client.post(f'{url}users/',
                                            data={'username': 'admin', 'email': 'uxui.des@gmail.com',
                                                  'password': '5118020Ago', 'is_active': True})
        self.get_token = self.client.post(f'{url}jwt/create/',
                                          data={'username': 'admin', 'password': '5118020Ago'})

        # self.response = self.client.force_authenticate(f'http://127.0.0.1:8000/api/v1/account/test/', user=self.create_user, token=self.get_token.get('success'))

    def test_auth(self):
        self.assertEqual(self.create_user.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.get_token.status_code, status.HTTP_200_OK)

