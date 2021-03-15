from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse("started")
    response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response