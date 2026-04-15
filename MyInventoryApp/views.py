from django.shortcuts import render, redirect, get_object_or_404
from MyInventoryApp.models import Supplier, WaterBottle, Accounts

logged_user = 0 #global key

# ============================================================
# Login and Signup

def login(request):
    global logged_user

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Accounts.objects.get(username=username, password=password)
            request.session['account_id'] = user.id
            logged_user = user.id
            return redirect('view_suppliers')

        except Accounts.DoesNotExist:
            return render(request, 'MyInventoryApp/login.html', {
                'error': 'Invalid login'
            })

    return render(request, 'MyInventoryApp/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Accounts.objects.filter(username=username).exists():
            return render(request, 'MyInventoryApp/signup.html', {
                'error': 'Account already exists'
            })

        Accounts.objects.create(username=username, password=password)

        return render(request, 'MyInventoryApp/login.html', {
            'success': 'Account created successfully'
        })

    return render(request, 'MyInventoryApp/signup.html')

def logout(request):
    global logged_user
    logged_user = 0
    return redirect('login')

# ====================================================================================================
# Suppliers and Bottles

def view_supplier(request):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    supplier_objects = Supplier.objects.all()
    account_id = request.session.get('account_id')
    return render(request, 'MyInventoryApp/view_suppliers.html', {'suppliers': supplier_objects, 'account_id': account_id})

def view_bottles(request):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles':bottle_objects})  

def view_bottle_details(request, pk):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    b = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/view_bottle_detail.html', {'b': b})

def delete_bottle(request, pk):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles')

def add_bottle(request):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    supplier_objects = Supplier.objects.all()

    if request.method == "POST":
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        color = request.POST.get('color')
        mouthsize = request.POST.get('mouthsize')
        quantity = request.POST.get('quantity')
        supplier_id = request.POST.get('supplier')
        supplier = get_object_or_404(Supplier, pk=supplier_id)

        WaterBottle.objects.create(
            SKU=sku,
            brand=brand,
            cost=cost,
            size=size,
            color=color,
            mouth_size=mouthsize,
            current_quantity=quantity,
            supplied_by=supplier
        )

        return redirect('view_bottles')
    
    return render(request, 'MyInventoryApp/add_bottles.html', {'suppliers': supplier_objects})

# ====================================================================================================
# Account Management

def change_password(request, pk):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    account = Accounts.objects.get(id=pk)

    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if current_password != account.password:
            return render(request, 'MyInventoryApp/change_password.html', {
                'account': account,
                'error': 'Current password is incorrect. '
            }) 

        if new_password == account.password:    
            return render(request, 'MyInventoryApp/change_password.html', {
                'account': account,
                'error': 'New password cannot be the same as the current password. '
            })
        
        if new_password != confirm_password:
            return render(request, 'MyInventoryApp/change_password.html', {
                'account': account,
                'error': 'New passwords do not match. '
            })
        
        
        account.password = new_password
        account.save()
        return redirect('manage_account', pk=pk)
    
    return render(request, 'MyInventoryApp/change_password.html', {'account': account})

def manage_account(request, pk):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    account = Accounts.objects.get(id=pk)
    return render(request, 'MyInventoryApp/manage_account.html', {'account': account})

def delete_account(request, pk):
    global logged_user
    if logged_user == 0:
        return redirect('login')
    
    account = Accounts.objects.get(id=pk)
    account.delete()
    return redirect('login')
