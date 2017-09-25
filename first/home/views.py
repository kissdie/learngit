from django.shortcuts import render
from django.utils import timezone
# Create your views here.

now = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
year = now.split(" ")[0].split("-")[0]
month = now.split(" ")[0].split("-")[1]
data = now.split(" ")[0].split("-")[2]
time = now.split(" ")[1]
tim = timezone.now()

dic = {
    'year': year,
    'month': month,
    'data': data,
    'time': time,
    "tim": tim,
}
def index(request):

    return render(request, "home.html", dic)

