from django.shortcuts import render
from web import models
from django.db.models import F, Q
import time
# Create your views here.


def notice(request):
    ret = models.Grant.objects.filter(Q(g_sid__s_name="宋江") & Q(g_record=1)).values_list("g_record", "g_sid__s_name",
                                                                                         "g_did__d_name", "g_time")
    for i in ret:
        print(type(i[3]))
        # print(time.strftime("%Y-%m-%d %H:%M:%S", i[3]))

    return render(request, "notice.html", {"ret": ret})


def help(request):
    return render(request,"help.html")


def tool(request):
    return render(request,"tool.html")


def test(request):
    return render(request,"test.html")
