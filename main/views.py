from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'app_name': 'Football Shop',
        'name': 'Renata Gracia Adli',
        'npm': '2406399705',
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username
    }
    return render(request, "main.html",context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'is_expensive': product.is_expensive,
            'user_id': product.user_id,
        }
        for product in products_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'is_expensive': product.is_expensive,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
@csrf_exempt
def register(request):
    if request.method == "POST":
        # Handle AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                form = UserCreationForm(data)
                
                if form.is_valid():
                    form.save()
                    return JsonResponse({
                        'success': True,
                        'message': 'Your account has been successfully created!'
                    }, status=201)
                else:
                    # Return form errors
                    errors = {}
                    for field, error_list in form.errors.items():
                        errors[field] = [str(error) for error in error_list]
                    return JsonResponse({
                        'success': False,
                        'errors': errors
                    }, status=400)
                    
            except json.JSONDecodeError:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid JSON data'
                }, status=400)
        
        # Handle normal form submission (fallback)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        # Handle AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                username = data.get('username')
                password = data.get('password')
                
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    response_data = {
                        'success': True,
                        'message': 'Login successful!',
                        'redirect_url': reverse('main:show_main')
                    }
                    response = JsonResponse(response_data)
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    return JsonResponse({
                        'success': False,
                        'error': 'Invalid username or password'
                    }, status=400)
                    
            except json.JSONDecodeError:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid JSON data'
                }, status=400)
        
        # Handle normal form submission (fallback)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        logout(request)
        return JsonResponse({
            'success': True,
            'message': 'Logout successful!',
            'redirect_url': reverse('main:login')
        })
    
    # Fallback for non-AJAX requests
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    # Validation
    if not name or not price or not description or not category:
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        product = Product.objects.create(
            user=user,
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
        )
        return JsonResponse({'message': 'Product created successfully', 'id': str(product.id)}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_POST
def update_product_ajax(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        
        # Check if user owns the product
        if product.user != request.user:
            return JsonResponse({'error': 'Permission denied'}, status=403)
        
        data = request.POST
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.description = data.get("description", product.description)
        product.thumbnail = data.get("thumbnail", product.thumbnail)
        product.category = data.get("category", product.category)
        product.is_featured = data.get("is_featured") == 'on'
        product.save()

        return JsonResponse({'message': 'Product updated successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_POST
def delete_product_ajax(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        
        # Check if user owns the product
        if product.user != request.user:
            return JsonResponse({'error': 'Permission denied'}, status=403)
            
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)