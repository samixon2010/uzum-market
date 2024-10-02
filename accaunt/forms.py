from django import forms
from .models import Category,Product, ProductImages, MyUser, Discount
from django.db.models.base import Model

class LogingForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(max_length=12)
	def __init__(self, *a, **b):
		super().__init__(*a, **b)
		self.fields['username'].widget.attrs.update({'class': 'form-control'})
		self.fields['password'].widget.attrs.update({'class': 'form-control'})
		
class CategoriForms(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']
		
class ProdactForms(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name','description','price','category']

	def __init__(self, *args, **kwargs) -> None:
		super(ProdactForms, self).__init__(*args, **kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({'class': 'form-control'})


class ProductImageForm(forms.ModelForm):
	class Meta:
		model = ProductImages
		fields = ['image']

	def __init__(self, *args, **kwargs) -> None:
		super(ProductImageForm, self).__init__(*args, **kwargs)
		for i in self.fields:
			self.fields[i].widget.attrs.update({'class': 'form-control'})

class EditForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name','description','price']

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ['username', 'first_name', 'last_name', 'password', 'adress', 'photo', 'phone']


class DiscountForm(forms.ModelForm):
	class Meta:
		model = Discount
		fields = ['product', 'name', 'image', 'discount']
	
		def __init__(self, *args, **kwargs) -> None:
			super(DiscountForm, self).__init__(*args, **kwargs)
			for i in self.fields:
				self.fields[i].widget.attrs.update({'class': 'form-control'})