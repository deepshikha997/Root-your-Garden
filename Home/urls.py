from django.urls import path
from . import views


urlpatterns = [
path('',views.index,name='index'),
path('garden',views.gardenform,name='garden'),
path('index2',views.index2,name="index2"),
path('About',views.about,name='abt'),
path('service',views.service,name='ser'),
path('service/<int:cid>',views.services,name='ser1'),
path('serviceone',views.serviceone,name='serviceone'),
path('servicetwo',views.servicetwo,name='servicetwo'),
path('service/servicetwo/<int:gid>',views.servicetwoo,name='servicetwoo'),
path('service3',views.service3,name='service3'),
path("addser",views.add_ser,name="addser"),
path('review',views.Review,name='rev'),
path('viewbookings',views.viewbook,name='viewbookings'),
path('checkout',views.checkout,name='checkout'),
path('billingdetails',views.billingdet,name='billingdetails'),
path('cash_on_delivery',views.cash_on_delivery,name='cash_on_delivery'),
path("blog-details-right-sidebar",views.blogs,name="blog-details-right-sidebar"),

path('cart',views.Cart,name='cart'),
path("tip",views.tips,name="tip"),
path("remove_ser",views.remove_ser,name="remove_ser"),
path("get_cart_data",views.get_cart_data,name="get_cart_data"),
path("process_payment",views.process_payment,name="process_payment"),
path("payment_done",views.payment_done,name="payment_done"),
path("payment_cancelled",views.payment_cancelled,name="payment_cancelled"),
path("contact",views.Contact,name="contact"),
path("feed",views.Feedback,name="fd")
]
