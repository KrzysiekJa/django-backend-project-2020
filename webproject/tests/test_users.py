from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from accounts.views import UserRegisterView, AdminRegisterView
from django.contrib.auth.models import User






class UserRegisterViewTest(APITestCase):
    
    url_path = 'localhost:8000/api/accounts/register/'
    
    def setUp(self):
        self.client = APIClient()
        
        self.user = User.objects.create_user(username='StochUser', email='stoch@stock.com', password='AdasLec100')
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)
    
    
    def testUnAuthenticatedUserRegisterView(self):
        self.client.force_authenticate(user=None)
        request = self.client.get(self.url_path)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def testGetUserRegisterView(self):
        request = self.client.get(path=self.url_path)
        
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data['username'], 'StochUser')
        self.assertEqual(request.data['email'], 'stoch@stock.com')
    
        
    def testPostUserRegisterView(self):
        data = {"username": "Shmidt", "email": "shmidt@stock.com", "password1": "niedlaMalysza111", "password2": "niedlaMalysza111"}
        request = self.client.post(path=self.url_path, data=data)
        
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.data.get('username'), 'Shmidt')
        self.assertEqual(request.dataget('email'), 'shmidt@stock.com')
    
    
    def tearDown(self):
        try:
            user = User.objects.get(username='StochUser')
            user.delete()
            user = User.objects.get(username='Shmidt')
            user.delete()

        except User.DoesNotExist:
            raise NameError("User doesnot exist")
        





class AdminRegisterViewTest(APITestCase):
    
    url_path = 'localhost:8000/api/accounts/admin/'
    
    def setUp(self):
        self.client = APIClient()
        
        self.admin = User.objects.create_user(username='KamilAdmin', email='kamil@stock.com', password='AdasLecLec100')
        self.admin.save()
        self.token = Token.objects.create(user=self.admin)
        self.api_authentication()
        
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)
        
        
    def testUnAuthenticatedAdminRegisterView(self):
        self.client.force_authenticate(user=None)
        request = self.client.get(self.url_path)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def testGetAdminRegisterView(self):
        request = self.client.get(path=self.url_path)
        
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data['username'], 'StochUser')
        self.assertEqual(request.data['email'], 'stoch@stock.com')
    
    
    def testPostAdminRegisterView(self):
        data = {"username": "Shmidt", "email": "shmidt@stock.com", "password1": "niedlaMalysza111", "password2": "niedlaMalysza111"}
        request = self.client.post(path=self.url_path, data=data)
        
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.data.get('username'), 'Shmidt')
        self.assertEqual(request.dataget('email'), 'shmidt@stock.com')
    
    
    def tearDown(self):
        try:
            admin = User.objects.get(username='KamilAdmin')
            admin.delete()
            admin = User.objects.get(username='Shmidt')
            admin.delete()  

        except User.DoesNotExist:
            raise NameError("User doesnot exist")




