from django.shortcuts import render
from web import models
from django.db.models import F, Q
import time


# 通知

def notice(request):
    # 后台读取当前登录用户的相关信息并返回给前台显示
    ret = models.Grant.objects.filter(Q(g_sid__s_name="宋江") & Q(g_record=1)).values_list("g_record", "g_sid__s_name",
                                                                                         "g_did__d_name", "g_time")
    for i in ret:
        print(type(i[3]))
        # print(time.strftime("%Y-%m-%d %H:%M:%S", i[3]))
    return render(request, "notice.html", {"ret": ret})


# 帮助

def help(request):
    return render(request, "help.html")


# 代码工具（暂空）

def tool(request):
    return render(request, "tool.html")


# 考试（暂空）

def test(request):
    return render(request, "test.html")
