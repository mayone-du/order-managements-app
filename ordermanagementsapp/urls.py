from django.urls import path, include
from .views import indexfunc, OrderList, signupfunc, loginfunc, logoutfunc, profilefunc, OrderCreate, OrderDetail, OrderUpdate, OrderDelete, readmefunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("index/", indexfunc, name="index"),
  path("list/", OrderList.as_view(), name="list"),
  path("signup/", signupfunc, name="signup"),
  path("login/", loginfunc, name="login"),
  path("logout/", logoutfunc, name="logout"),
  path("profile/<int:user_id>/", profilefunc, name="profile"),
  path("create/", OrderCreate.as_view(), name="create"),
  path("detail/<int:pk>", OrderDetail.as_view(), name="detail"),
  path("update/<int:pk>", OrderUpdate.as_view(), name="update"),
  path("delete/<int:pk>", OrderDelete.as_view(), name="delete"),
  path("readme/", readmefunc, name="readme"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)