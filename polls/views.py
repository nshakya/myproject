# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
	
# recall or note that %s means, "subsitute in a string"

def detail(request, poll_id):
    return HttpResponse("You're looking at poll <strong> %s. </strong>"  % ( poll_id,))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll <strong> %s. </strong>" % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll <u> %s. </u>" % (poll_id,))
   
def redirect_to_polls(request):
    return HttpResponseRedirect('/polls/')