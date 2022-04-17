
from django.urls import path

from . import views


urlpatterns = [
    path("",views.home),
    path("veg",views.veg),
    path("register",views.register),
    path("bill",views.bill),
    path("snacks",views.snacks),
    path("forget_pass",views.forget_pass),
    path("soft_drinks",views.soft_drinks),
    path("thanq",views.thanq),
    path("super_admin",views.super_admin),
    path("login_super_admin",views.login_super_admin),
    path("admin1",views.admin1),
    path("add_item",views.add_item),
    path("change",views.change),
    path("login_admin",views.login_admin),
    path("login",views.login),
    path("reset",views.reset),
    path("delete_item",views.delete_item),
    path("non_veg",views.non_veg),
    path("change_order",views.change_order),
    path("cancel",views.cancel),
]