from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
  # return HttpResponse("Shwmae, byd!")
  context = { 'message': 'Shwmae, byd'}
  textentered = request.GET.get('textbox')
  if not textentered:
    context['formtext'] = 'you didnt type anything'
  else:
    context['formtext'] = textentered
  
  return render(request, 'hello/index.html', context=context)
