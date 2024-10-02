from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Category, Product, Comment, Registration, Discount, Like
from .forms import LogingForm,CategoriForms,ProdactForms, ProductImageForm, EditForm, RegistrationForm, DiscountForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F, Count, Max
# from django.views.generic import DeleteView
from .models import Product
from django.urls import reverse_lazy

# def category(request):
# 	return render(request, 'creat_cate.html')


@login_required(login_url='login')
def user_products(request):
	my_products = Product.objects.filter(user=request.user)
	ctx = {
		'my_products' : my_products
	}
	return render(request, 'profile.html', ctx)

def register(request):
	form = RegistrationForm()
	if request.POST:
		form = RegistrationForm(request.POST, files=request.FILES)
		if form.is_valid():
			a = form.save()
			parol = form.cleaned_data['password']
			a.set_password(parol)
			a.save()
			return redirect('home')
	return render(request, 'contact.html', {"form":form})


def home(request):
	discount_p = Discount.objects.all()[0:3]
	categories = Category.objects.all()
	products = Product.objects.all()
	# left_products = Product.objects.annotate(juft=F('id')%2).filter(juft=True)
	# right_products = Product.objects.annotate(juft=F('id')%2).filter(juft=False)
	category = request.GET.get('category')
	if category:
		products = Product.objects.filter(category__id=category)
	products = {
		'products': products,
		'category' : categories,
		'discount' : discount_p
		  }
	print(request.POST)
	
	if request.POST:
		id = request.POST['p_id']
		product = Product.objects.get(id=id)
		like, created = Like.objects.get_or_create(
			product = product
		)
		if request.user in like.user.all():
			like.user.remove(request.user)
		else:
			like.user.add(request.user)
			like.save()
			# return redirect(reverse('home')+?)
			return redirect(reverse('home') + f"#{id}" )
	return render(request, 'index.html', products)

@login_required(login_url='login')
def detail(request, id):
	a = Product.objects.get(id=id)
	similar_products = Product.objects.filter(category=a.category).exclude(id=a.id)
	i = a.tags.all()

	category = request.GET.get('category')
	if category:
		a = Product.objects.filter(category__id=category)
	print("----")
	print(i)
	print("----")
	if request.POST.get('izoh'):
		name = request.POST['name'] 
		Comment.objects.create(
			comment = request.POST['izoh'],
			product = a,
			user = request.user	
		)
		return redirect(reverse('detail', args=[a.id]) + f"#{name}" )
	
	elif request.POST.get('reply'):
		comment = Comment.objects.get(id=request.POST['comment_id'])
		name = request.POST['name'] 
		Comment.objects.create(
			comment = request.POST['reply'],

			product = a,
			user = request.user,
			reply = comment
		)
		return redirect(reverse('detail', args=[a.id]) + f"#{name}")
	return render(request, 'single-post.html', {'a':a, 'similar_products' : similar_products, 'tags' : i, 'category' : Category.objects.all()})

def contact(request):
	categories = Category.objects.all()
	if request.POST:
		Registration.objects.create(
			name=request.POST['name'],
			last_name=request.POST['last_name'],
			email=request.POST['email'],
			password=request.POST['password'],
			phone_number=request.POST['phone_number']
		)
		return redirect('home')
	return render(request, 'contact.html', {'category':categories})

def about(request):
	categories = Category.objects.all()
	return render(request, 'about.html', {'category':categories})

def search(request):
	return render(request, 'search-result.html')

def category(request):
	form= CategoriForms()
	if request.POST:
		form=CategoriForms(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	return render(request,'creat_cate.html',{'form':form})


def Login(request):
	form = LogingForm()
	if request.POST:
		print('post')
		# if form.is_valid():
		# 	print('valid')
		a = request.POST.get('username')
		b = request.POST.get('password')
		user = authenticate(request, username=a,password=b)
		if user is not None:
			print('user')
			login(request, user)
			return redirect('home')
	return render(request,'login.html',{'form':form})

def Logout(request):
	logout(request)
	return redirect('home')

def createlon(request):
	categories = Category.objects.all()
	form= ProdactForms()
	if request.POST:
		form=ProdactForms(request.POST, files=request.FILES)
		if form.is_valid():
			reklama=form.save(commit=False)
			reklama.connect2=request.user
			reklama.save()
			return redirect("create_image", reklama.id)
	return render(request,'creat.html',{'form':form, 'category':categories})


def create_image(request, id):
	offer = 'Rasm qoshishni xohlaysizmi?'
	form = ProductImageForm()
	if request.POST:
		form = ProductImageForm(files=request.FILES)
		if form.is_valid():
			new_image = form.save(commit=False)
			new_image.product = Product.objects.get(id=id)
			new_image.save()


	return render(request, 'creat.html', {'form': form, 'offer': offer})

def edit(request,id):
	a = Product.objects.get(id=id)
	form = ProdactForms(instance=a)
	if request.POST:
		form = EditForm(request.POST,instance=a, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request,'edit.html',{'form':form})
# Create your views here.

def delete(request, id):
	a = Product.objects.get(id=id)
	a.delete()
	return redirect('home')

# class DeleteView(DeleteView):
# 	model = Product
# 	template_name = 'delet.html'
# 	success_url = reverse_lazy('home')


def discount(request):
	form = DiscountForm()
	if request.POST:
		form = DiscountForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request, 'discount.html', {'form' : form})