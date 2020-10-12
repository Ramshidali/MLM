from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from mlmm.models import registration,wallet,referel_id
from django.db.models import Sum
from django.contrib.auth import authenticate
from django.contrib import messages

import random
import string
import re

# Create your views here.

def index(request):
    return render(request,'index.html')


def register_page(request):
    return render(request,'registration.html')


def register(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']

    phone_regex = '[6-9]{1}[0-9]{9}'
    phone = request.POST['phone']
    if (re.search(phone_regex, phone)) is None:
        messages.success(request, 'Invalid Phone Number Pattern...!\nFirst digit 6-9')
        return render(request, 'registration.html')

    email_regex = '[a-z0-9._%+-]{3,}@[a-z]{3,}([.]{1}[a-z]{2,}|[.]{1}[a-z]{2,}[.]{1}[a-z]{2,})'
    email = request.POST['email']
    if (re.search(email_regex, email)) is None:
        messages.success(request, 'Invalid Email Pattern...!\nexample@mail.com')
        return render(request, 'registration.html')

    password = request.POST['password']
    c_password = request.POST['c_password']
    referedid = request.POST['refid']

    if referedid != "":
        refid = referel_id.objects.get(reference=referedid)
        wallet_cash_reference = wallet(uid=refid.uid, wallet_amount=10)
        wallet_cash_reference.save()


    if password == c_password:
        user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name,
                                        email=email)
        user.save()

        reg = registration(id=user, phone=phone)
        reg.save()
        wallet_cash_new_user = wallet(uid=user, wallet_amount=100)
        wallet_cash_new_user.save()

        def get_random_string(length):
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(length))
            ref_result = result_str

            ref = referel_id(uid=user, reference=ref_result)
            ref.save()
        get_random_string(8)



    else:
        return '''
                            <script>
                                alert('Password not matching...!!!')
                            </script>

                '''
        return redirect('/registration_page/')
    return redirect('/registration_page/')


def signin(request):
    if request.method == 'GET':
        return render(request, 'index.html')


    username = request.POST['u_name']
    passwrd = request.POST['password']


    user = authenticate(request, username=username, password=passwrd)
    if user is None:
        if user.is_active:
            index(request, user)
        else:
            return render(request, 'registration.html')
    else:
        request.session['id'] = user.pk
        user = User.objects.get(pk=request.session['id'])

        ref_id = referel_id.objects.get(uid=user.id)
        wallet_balance = wallet.objects.filter(uid=user.id).aggregate(Sum('wallet_amount'))


        context = {
            'ref_id': ref_id,
            'w_balance': wallet_balance,
        }


        return render(request,'view_childs.html',context)




