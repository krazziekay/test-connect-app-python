from django.http import HttpResponse
from django.http import JsonResponse
import json

BASE_URL="https://pythonapp.public.atlastunnel.com"

def index(request):
    responseData = {
       'name': 'Test Connect App Python',
       'description': 'Atlassian Connect app for Test',
       'key': 'com.sample.connect-python',
       'baseUrl': BASE_URL,
       'vendor': {
           'name': 'Python connect app sample',
           'url': 'https://github.com/krazziekay/test-connect-app-python'
       },
       'authentication': {
           'type': 'none'
       },
       'apiVersion': 1,
       'modules': {
           'postInstallPage': {
               'url': '/api',
               'key': 'connect-app-index',
               'name': {
                   'value': 'Index'
               },
           },
           'adminPages': [{
               'url': '/api',
               'key': 'connect-app-admin',
               'name': {
                   'value': 'Index'
               },
               'location': 'admin_plugins_menu/test-connect-app'
           }],
           'webSections': [
           		{
           			'key': "test-connect-app",
           			'location': "admin_plugins_menu",
           			'name': {
           				'value': "Test Connect App"
           			}
           		}
           	],
           'generalPages': [
               {
                   'url': '/api/contact',
                   'key': 'connect-app-contact',
                   'location': 'none',
                   'name': {
                       'value': 'Contact'
                   }
               },
               {
                   'url': '/api/info',
                   'key': 'connect-app-info',
                   'location': 'none',
                   'name': {
                       'value': 'Info'
                   }
               }
           ]
       }
    }

    return HttpResponse(json.dumps(responseData), content_type="application/json")