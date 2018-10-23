from django.shortcuts import render
from need_fix.models import Record


def index(request):
    query_list = Record.objects.all().order_by("status", "person", "priority")
    print(query_list)
    context = {
        "query_list": query_list,
    }
    return render(request, "need_fix/index.html", context)
