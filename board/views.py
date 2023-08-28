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


def Page3View(request):
  # creating class
  class obj:
    def __init__(self, title, total, ytd):
      self.title = title
      self.total = total
      self.ytd = ytd

  # creating list
  list_1 = []
  list_2 = []

  # appending instances to list
  list_1.append(obj('Fatality', 0, 0))
  list_1.append(obj('Severe Accident', 0, 0))
  list_1.append(obj('Serious Safety Events', '<=7', 0))
  list_1.append(obj('Total Recordable FR', '<=0.35', 0))
  list_1.append(obj('Lost Work Day FR', '<=0.12', 0))

  list_2.append(obj('Near Miss Rate', 45, 0))
  list_2.append(obj('Safety Observations', '95%', 0))
  list_2.append(obj('Safety Hours Trained (% man hrs worked)', '1.5%', 0))

  context = {
    'list_1': list_1,
    'list_2': list_2,
  }
  return render(request, 'board/page3.html', context)