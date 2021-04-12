from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
import random
from django.views.generic import ListView, DetailView, View
from .models import Order, cancel_order_for_money_back
from home.models import customer_more_information, products
# Create your views here.
# from datetime import datetime
import datetime

import stripe
# stripe Secret key
stripe.api_key = "sk_test_51IWuSRFzvY3Oon8KHXlURApAt4rjhN1qKfh37Xvcwam0uzfvzZt8o3TJCirb5uFParGlho3a15S6V2s0mZLXsaOg00woMU6Fen"

# for my order page to show customer ordered lists
def my_orders(request):
    # get user
    user = request.user
    # filter those order, which are same user and ordered Boolean true
    get_all_order = Order.objects.filter(user=user, ordered=True)
    context = {'get_all_order':get_all_order}
    return render(request, 'my_order.html', context)

# customer make order cancel
def customer_canceled_order(request):
    # to get current time and date
    now_time = datetime.datetime.now()
    print(now_time)

    # get order id to get the details
    order_id = request.POST.get('order_id')
    get_order = Order.objects.get(id=order_id)

    # get time and date of order time
    order_time = get_order.order_date
    print(order_time)

    date_time_str = order_time

    # now need to measurement of different between of order time and now
    # because we need to know is that 24 hours gone or note
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    print(date_time_obj.date())

    differnt_time = now_time - date_time_obj
    print(differnt_time)
    print(differnt_time.days)
    print(differnt_time.seconds)
    print(differnt_time.microseconds)

    # get time different in days
    differnt_time_days = differnt_time.days

    # if days less than 1 that means less than 24 hours
    if differnt_time_days < 1:
        get_order.customer_cancel_order=True
        get_order.save()
        messages.success(request, "You Will Get Your Money Back in 3 working days from Admin. Because You have canceled This Order in 24 Hours !")

        # if days less than 1 that means less than 24 hours save a new table for admin to pay back the customer
        money_back_admin = cancel_order_for_money_back(user=request.user, order=get_order)
        money_back_admin.save()

        return redirect('my_order_details' , get_order.id)
    else:
        get_order.customer_cancel_order = True
        get_order.save()
        messages.success(request, "You Will Not Get Your Money Back. Because You didn't cancel This Order in 24 Hours !")
        return redirect('my_order_details', get_order.id)


# custmer order details page
# get order id by passing id in link
def my_order_details(request, pk):
    # get the details of order
    get_the_order = Order.objects.get(id=pk)
    context = {'get_the_order':get_the_order}
    return render(request, 'my_order_details.html', context)

# cart page
def cart(request):
    return render(request, 'shoping-cart.html')

# for Checkout
def checkout(request):
    if request.method =="POST":
        # get all input
        prod_details = request.POST.get('prod_details')
        checkout_money = request.POST.get('checkout_money')

        all_prod = request.POST.get('all_prod')
        print(all_prod)

        all_prod_price = request.POST.get('all_prod_price')
        all_prod_qty = request.POST.get('all_prod_qty')
        all_prod_price_qty = request.POST.get('all_prod_price_qty')
        # print('total')
        # print(checkout_money, prod_details)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zip = request.POST.get('zip')


        # print(full_address, city, postal_code, country, phone)

        # save all the order to database by loop
        for i in all_prod:
            print(i)
            # print(type(i))

            check_integer = i.isnumeric()
            print(check_integer)

            # if the value is integer
            if check_integer:
                print('yes')
                print(i)
                print(type(i))

                lesson_Id = int(i)
                print(type(lesson_Id))

                # by id get the lesson details
                get_lesson = products.objects.get(id=lesson_Id)
                print(get_lesson)

                # lesson single price
                single_price = get_lesson.product_price
                # lesson instructor
                instructor = get_lesson.Intructor

                # make random order ID
                random_num = random.randint(2345678909800, 9923456789000)

                uniqe_confirm = Order.objects.filter(order_id=random_num)
                # print(random_num)

                while uniqe_confirm:
                    random_num = random.randint(234567890980000, 992345678900000)
                    if not Order.objects.filter(order_id=random_num):
                        break
                # print(random_num)

                user = request.user
                # save order
                post_order = Order(user=user, Lesson=get_lesson, Instructor=instructor, order_id=random_num, Lesson_price=single_price,
                                   first_name=first_name, last_name=last_name, email=email, phone=phone,
                                   address=address, zip=zip, order_date=datetime.datetime.now())
                post_order.save()
            else:
                print('no')


        Thank = True
        return render(request, 'checkout.html', {'Thank': Thank})

    else:
        # if customer is loged in:
        if request.user.is_authenticated:
            user=request.user
            # filter those orders which have not payment yet
            order = Order.objects.filter(user=user, ordered=False)
            # print(order)
            # for new order customer have to payment the remain unpayment order
            if order:
                messages.info(request, 'You Have a Order Remain to Payment !! To Order New, You Have to Pay The first One.')
                return redirect('payment')
            else:
                # get details about customer
                filter_user=customer_more_information.objects.filter(Customer=user)
                if filter_user:
                    get_user=customer_more_information.objects.get(Customer=user)
                    context4 = {'get_user':get_user}
                    return render(request, 'checkout.html', context4)
                else:
                    # return render(request, 'checkout.html')
                    messages.info(request, 'Please Give Us Some Information.')
                    return redirect('edit_profile')
        else:
            return redirect('signup_login')

class PaymentView(View):
    # for get
    def get(self, *args, **kwargs):
        user = self.request.user
        # get the order details which is remian to payment
        order = Order.objects.filter(user=user, ordered=False)
        print(order)

        sum_of_bill=0

        # making sum of order price
        for i in order:
            print(i)
            sum_of_bill = sum_of_bill + int(i.Lesson_price)
        print(sum_of_bill)

        # making condition for discount counting
        if sum_of_bill >= 100:
            sum_of_bill = (sum_of_bill / 100) * 70
        else:
            sum_of_bill = (sum_of_bill / 100) * 90

        sum_of_bill = "%0.2f" % sum_of_bill

        context = {
            'sum_of_bill': sum_of_bill,
            'order': order,
            "DISPLAY_COUPON_FORM": False

        }
        return render(self.request, 'payment.html', context)

    # for post
    def post(self, *args, **kwargs):
        print(self.request.user)
        # user details
        user=self.request.user

        # filter those order, which are not paid and same user
        order = Order.objects.filter(user=user, ordered=False)
        print(order)

        sum_of_bill = 0
        # making condition for discount counting
        for i in order:
            print(i)
            sum_of_bill = sum_of_bill + int(i.Lesson_price)
        print(sum_of_bill)


        try:
            # try for making payment from stripe getway
            customer = stripe.Customer.create(
                email=self.request.user.email,
                description=self.request.user.username,
                source=self.request.POST['stripeToken']
            )
            amount = int(sum_of_bill)

            # making condition for discount counting
            if amount>100:
                a = amount*70
                print(a)
            else:
                a=amount*90
                print(a)

            charge = stripe.Charge.create(
                amount=a,
                currency="gbp",
                customer=customer,
                description="Payment for 828 Driving School",
            )

            # making the orders paid and make ordered boolean True
            for i in order:
                i.ordered = True
                i.save()

                last_order_id=i.id

            order_cus = Order.objects.get(id=last_order_id)

            # sending email to customer about the order
            email_for_buy = render_to_string(
                'email_for_buy.html',
                {

                    'first_name': self.request.user.first_name,
                    'last_name': self.request.user.last_name,
                    'order': order,
                    'order_cus': order_cus,
                }
            )

            email=self.request.user.email
            send_mail(
                'Purchase Order',  # subject
                email_for_buy,  # massage
                '',  # from email
                [email],  # to email

                fail_silently=True,
            )

            messages.success(self.request, 'Payment was Successfull !!')

        # if there any error in payment
        # if try is not proper working then
        except stripe.error.CardError as e:
            messages.info(self.request, f"{e.error.message}")
            return redirect('index')

        except stripe.error.RateLimitError as e:
            messages.info(self.request, f"{e.error.message}")
            return redirect('index')
        except stripe.error.InvalidRequestError as e:
            messages.info(self.request, "Invalid Request !")
            return redirect('index')
        except stripe.error.AuthenticationError as e:
            messages.info(self.request, "Authentication Error !!")
            return redirect('index')
        except stripe.error.APIConnectionError as e:
            messages.info(self.request, "Check Your Connection !")
            return redirect('index')
        except stripe.error.StripeError as e:
            messages.info(self.request, "There was an error please try again !")
            return redirect('index')
        except Exception as e:
            messages.info(self.request, "A serious error occured we were notified !")
            return redirect('index')

        return redirect('index')
