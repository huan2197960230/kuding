from django.shortcuts import render

# Create your views here.


def notice(request):
    return render(request,"notice.html")


def help(request):
    return render(request,"help.html")


def tool(request):
    return render(request,"tool.html")


def test(request):
    return render(request,"test.html")
