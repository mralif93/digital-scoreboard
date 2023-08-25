from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def IndexView(request):
  now = timezone.now()
  context = {
    # 'now': now,
  }
  return render(request, 'board/index.html', context)