from django.http import HttpResponse
from django.template import loader

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