from django.shortcuts import render

# Create your views here.
def LoginView(request):
  context = {}
  return render(request, 'users/login.html', context)