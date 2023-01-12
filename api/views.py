from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_exempt


# Need this decorator so that this page can be viewed within the iframe
# Source: https://stackoverflow.com/questions/33267383/how-to-configure-x-frame-options-in-django-to-allow-iframe-embedding-of-one-view#answer-33267908
@xframe_options_exempt
def index(request):
  template = loader.get_template('index.html')
  context = {
    'title': 'Index',
    'body': 'This is the index page',
    'links': [
        {
          'url': '/api/info',
          'text': 'Info'
        },
        {
          'url': '/api/contact',
          'text': 'Contact'
        }
    ]

  }
  return HttpResponse(template.render(context, request))

@xframe_options_exempt
def info(request):
  template = loader.get_template('index.html')
  context = {
    'title': 'Info',
    'body': 'This is the info page',
    'links': [
        {
          'url': '/api/',
          'text': 'Index'
        },
        {
          'url': '/api/contact',
          'text': 'Contact'
        }
    ]
  }
  return HttpResponse(template.render(context, request))

@xframe_options_exempt
def contact(request):
  template = loader.get_template('index.html')
  context = {
    'title': 'Contact',
    'body': 'This is the contact page',
    'links': [
        {
          'url': '/api/',
          'text': 'Index'
        },
        {
          'url': '/api/info',
          'text': 'Info'
        }
    ]
  }
  return HttpResponse(template.render(context, request))