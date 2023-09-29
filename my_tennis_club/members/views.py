from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers  = Member.objects.all().values()
  template = loader.get_template('all_members.html')

  context = {
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context,request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember' : mymember,
  }

  return HttpResponse(template.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context =  {
    'fruits': ['Banana','Durian','Cherry'],
    'xx': ['Banana','Durian','Cherry'],
    'yy': ['Banana','Durian','Cherry'],
    'firstname': 'Linus',
    'mymembers' : mymembers,
    'greetings' : 1 , 
    'day': 'monday',
    'somenumber4': 4,
    'somenumber5': 5,
    'somenumber6': 6,
  }
  return HttpResponse(template.render(context,request))
