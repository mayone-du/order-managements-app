from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import OrderManagementsModel
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum, Avg

# Create your views here.

def indexfunc(request):
  return render(request, "index.html", {})



class OrderList(ListView):
  template_name = "list.html"
  model = OrderManagementsModel

  def get_queryset(self):
    return OrderManagementsModel.objects.filter(create_user=self.request.user).order_by("delivery_date")
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["order_price"] = OrderManagementsModel.objects.filter(create_user=self.request.user).aggregate(total_num=Sum("order_price"))
    context["sales_amount"] = OrderManagementsModel.objects.filter(create_user=self.request.user).aggregate(total_num=Sum("sales_amount"))
    context["review_count_avg"] = OrderManagementsModel.objects.filter(create_user=self.request.user).aggregate(avg_count=Avg("review_count"))
    context["all_orderes"] = OrderManagementsModel.objects.filter(create_user=self.request.user).count()
    context["un_delivered_list"] = OrderManagementsModel.objects.filter(create_user=self.request.user, delivery_date__isnull=True).order_by("delivery_date")
    context["un_delivered_count"] = OrderManagementsModel.objects.filter(create_user=self.request.user, delivery_date__isnull=True).count()
    context["delivered_list"] = OrderManagementsModel.objects.filter(create_user=self.request.user, delivery_date__isnull=False).order_by("delivery_date")
    context["delivered_count"] = OrderManagementsModel.objects.filter(create_user=self.request.user, delivery_date__isnull=False).count()
    return context

def signupfunc(request):
  if request.method == "POST":
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    try:
      new_user = User.objects.create_user(username, email, password)
    except:
      return render(request, "signup.html", {"error":True})
    return render(request, "signup.html", {"success":True})

  else:
    return render(request, "signup.html", {"first":True})


def loginfunc(request):
  if request.method == "POST":
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(username=username, email=email, password=password)
    if user is not None:
      login(request, user)
      return redirect("list")
    else:
      return render(request, "login.html", {"error":True})
  else:
    return render(request, "login.html", {})


@login_required
def logoutfunc(request):
  if request.method == "POST":
    logout(request)
    return redirect("login")
  return render(request, "logout.html", {})


@login_required
def profilefunc(request, user_id):
  profile = get_object_or_404(User, pk=user_id)
  return render(request, "profile.html", {"profile":profile})


class OrderCreate(CreateView):
  template_name = "create.html"
  model = OrderManagementsModel
  fields = ("ordered_services", "ordered_services_memo", "thumbnail", "ordered_media", "personal_or_corporate", "option", "order_date", "delivery_date", "order_price", "sales_amount", "create_user", "review_count", "review_text")
  success_url = reverse_lazy("list")



class OrderDetail(DetailView):
  template_name = "detail.html"
  model = OrderManagementsModel



class OrderUpdate(UpdateView):
  template_name = "update.html"
  model = OrderManagementsModel
  fields = ("ordered_services", "ordered_services_memo", "thumbnail", "ordered_media", "personal_or_corporate", "option", "order_date", "delivery_date", "order_price", "sales_amount", "create_user", "review_count", "review_text")
  success_url = reverse_lazy("list")


class OrderDelete(DeleteView):
  template_name = "delete.html"
  model = OrderManagementsModel
  fields = ("ordered_services", "ordered_services_memo", "thumbnail", "ordered_media", "personal_or_corporate", "option", "order_date", "delivery_date", "order_price", "sales_amount", "create_user", "review_count", "review_text")
  success_url = reverse_lazy("list")



def readmefunc(request):
  return render(request, "readme.html", {})