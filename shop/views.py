from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from . import models


def list_item(request):
    items = models.Item.objects.all()
    context = {
        "items": items,
    }
    if request.method == "POST":
        return redirect(reverse("detail_item", kwargs={"item_id": request.POST.get("item_id")}))
    return render(request, "list_item.html", context)


def detail_item(request, item_id):
    try:
        item = models.Item.objects.get(id=item_id)
    except Exception:
        print("Нет такого айди")
        return redirect(reverse("list_item"))
    return render(request, "detail_item.html", {"item": item})




