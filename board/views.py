from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def Page1View(request):
  now = timezone.now()
  context = {
    # 'now': now,
  }
  return render(request, 'board/page1.html', context)


def Page2View(request):
  # creating class
  class obj:
    def __init__(self, title, total):
      self.title = title
      self.total = total

  # creating list
  list = []

  # appending instances to list
  list.append(obj('Lost Time Injury', 0))
  list.append(obj('Medical Treatment Case', 0))
  list.append(obj('First Aid Case', 0))
  list.append(obj('Fire / Explosion', 0))
  list.append(obj('Lost of Primary Containment', 0))
  list.append(obj('Property / Equipment', 0))
  list.append(obj('Near Miss', 0))
  list.append(obj('Unsafe Act Unsafe Condition', 0))

  context = {
    'list': list,
  }
  return render(request, 'board/page2.html', context)