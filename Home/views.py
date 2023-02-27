from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from Home.models import *
from django.contrib.auth.models import User

# Create your views here
def index(request):
   dic={}
   cat=Category.objects.all().order_by("name_cat")
   dic["cate"]=cat
   return render(request,'index.html',dic)

def index2(request):
    ind=Nursery.objects.filter(usr_id=request.user.id)
    if len(ind)>0:
        ind=index2.objects.filter(usr_id=request.user.id)
    return render (request,"index2.html",{"ind":ind})

def services(request,cid):
   dic={}
   cat=Category.objects.get(id=cid)
   ser=Nursery.objects.filter(cate=cat).order_by("name_nur")
   dic["serv"]=ser
   return render(request,'serviceone.html',dic)

def service(request):
   dic={}
   ser=Service.objects.all().order_by("name_ser")
   dic["serv"]=ser
   return render(request,'serviceone.html',dic)
def serviceone(request):
   dic={}
   ser=Service.objects.all()
   dic["serv"]=ser
   return render(request,'serviceone.html',dic)

def servicetwo(request):
   dic={}
   ser=Service.objects.all()
   dic["se"]=ser
   return render(request,'servicetwo.html',dic)
def servicetwoo(request,gid):
   dic={}
   cat=Nursery.objects.get(id=gid)
   ser=Service.objects.filter(nur=cat)
   dic["se"]=ser
   return render(request,'servicetwo.html',dic)

def service3(request):
   dic={}
   ser=Service.objects.all()
   dic["serv"]=ser
   return render(request,'service3.html',dic)
   
def gardenform(request):
   dic={}
   categ=Category.objects.all()
   dic["cate"]=categ
   gar=Nursery.objects.filter(usr_id=request.user.id)
   dic["gar"]=gar
   return render(request,'gardenform.html',dic)


def add_ser(request):
   if request.method=="POST":
      namesr=request.POST['ser1']
      desser=request.POST['descser1']
      pricesr=request.POST['priceser1']
      cat=request.POST['ct']
      nur=request.POST['nur']
      nr=get_object_or_404(Nursery,id=nur)
      ct=get_object_or_404(Category,id=cat)
      addser=Service(nur=nr,name_ser=namesr,desc_ser=desser,price_ser=pricesr)
      addser.save()
      if "imgs" in request.FILES:
                img=request.FILES["imgs"]
                addser.img_pro=img
                addser.save()
      messages.info(request,"Services and Image Added Successfully")
      return redirect("garden")
   return render(request,'gardenform.html')

      

def Cart(request):
   display={}
   item=cart.objects.filter(usr_id=request.user.id,status=False)
   display["item"]=item
   if request.user.is_authenticated:
     if request.method=="POST":
      sid=request.POST["sid"]
      quantity=request.POST["qty"]
      is_exist=cart.objects.filter(service_id=sid,usr_id=request.user.id,status=False)
      if len(is_exist)>0:
         display["msg"]="Item already exists in your cart."
      else:
         srvc=get_object_or_404(Service,id=sid)
         usr=get_object_or_404(User,id=request.user.id)
         crt=cart(usr=usr,service=srvc,quantity=quantity)
         crt.save()
         display["msg"]="{}Added in your cart.".format(srvc.name_ser)
         display["cls"]="alert alert success"
   else:
         display["status"]="Please login first to view your cart."
   return render(request,"cart.html",display)

def get_cart_data(request):
   item=cart.objects.filter(usr_id=request.user.id,status=False)
   sale,quantity=0,0

   for i in item:
      sale+=float(i.service.price_ser)*i.quantity
      quantity=quantity+int(i.quantity)
   resp={"quan":quantity,"tot":sale} #dictionary
   return JsonResponse(resp)

def remove_ser(request):
   if "delete_cart" in request.GET:
      id=request.GET["delete_cart"]
      cartobj=get_object_or_404(cart,id=id)
      cartobj.delete()
   return HttpResponse(1)

def process_payment(request):
    items = cart.objects.filter(usr_id__id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.service.name_ser)+"\n"
        p_ids += str(j.service.id)+","
        amt += float(j.service.price_ser)/77
        inv +=  str(j.id)
        cart_ids += str(j.id)+","

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")

def about(request):
   return render(request,'about.html')
# def pamph(request):

#    dis=Pamplate.objects.all()

#    return render(request,"servicetwo.html",{"guide":dis})
def Contact(request):
   usr=contact.objects.filter(usr_id=request.user.id)
   if request.method=="POST":
      phone=request.POST['phone']
      content=request.POST['content']
      print(phone, content)
      if len(phone)<10 or len(content)<4:
         messages.info(request, "Field Error")
      else:
         usr=get_object_or_404(User,id=request.user.id)
         con=contact(usr=usr,phone=phone,msg=content)
         con.save()
         messages.info(request, "Message send successfully...")
         return render('contact')
   return render(request, "contact.html")  

def Feedback(request):
    usr=get_object_or_404(User,id=request.user.id)
    prf=profile.objects.get(usr_id=request.user.id)
    if request.user.is_authenticated:
        if request.method=='POST':
            
            mes=request.POST['comments']
            rate=request.POST['rat']
            
            fdcr=feedback(user=usr,prf=prf,msg=mes,rating=rate)
            fdcr.save()
            messages.success(request, "Review Posted")
            return redirect('fd')
            
    return render(request,"review.html") 
def Review(request):
   return render(request,"review.html")

def cash_on_delivery(request):
    items = cart.objects.filter(usr_id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.service.name_ser)+"\n"
        p_ids += str(j.service.id)+","
        amt += float(j.service.price_ser)/75
        inv +=  str(j.id)
        cart_ids += str(j.id)+","
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    return redirect('viewbookings')

def viewbook(request):
    obj=Order.objects.filter(cust_id=request.user.id)
   #  bkngs=billingdetails.objects.filter(usr_id=request.user.id)
    return render(request,"viewbookings.html",{"orderview":obj})
def checkout(request):
   return render(request,"checkout.html")

def tips(request):
   tp={}
   tip=tips.objects.all()
   tp["tip"]=tip
   return render(request,"tips.html",tp)

def blogs(request):
   return render(request,"blog-details-right-sidebar.html")
   
def billingdet(request):
    usr=billingdetails.objects.filter(usr_id=request.user.id)
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        em=request.POST['email']
        ph_pro=request.POST['ph_pro']
        state=request.POST['state']
        city=request.POST['city']
        street=request.POST['street']
        od=request.POST['details']
        usr=get_object_or_404(User,id=request.user.id)
        billdetails=billingdetails(usr=usr,fname=fname,lname=lname,email=em,ph_pro=ph_pro,state=state,city=city,street=street,det=od)
        billdetails.save()
        messages.info(request,"Billing Details have been added")
    return render(request,"checkout.html")

# def blog1(request):
#    return render(request,'blog-details-right-sidebar.html')
  







# def category(request):

#    return render(request,'service-one.html',dic)
 #second
    #go to views.py me yhe code karna h
    #cr=Service.objects.all()
   # {"cro":cr}
#first fetching line 348 in services
  #services two.html
  # #go to page templates services.html
  #add {% for i in  cro(it is the project name)%}  after the div class (remove the image)
  #add img_ser from models.py
  #{% endfor %}

#third
  # #go to setting.py go after static line 128
  #MEDIA_URL="/media/"
  # MEDIA_ROOT=os.path.join(BASE_DIR,"media")
  # go to urls.py of rug
  # line 18,19,20
  # from django.con.urls.static import static
  #from django.con.urls import url #remove the line 
  #from django.conf import settings
  #line 24 after] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

  # go to admin panel in chrome
  # click-> services add services then->go to veiw site click on the one part of the site it show the database