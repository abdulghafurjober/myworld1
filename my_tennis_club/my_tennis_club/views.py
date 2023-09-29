from django.http import HttpResponse
from django.template import loader
import mimetypes

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/html", ".html", True)
mimetypes.add_type("application/javascript", ".js", True)

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())