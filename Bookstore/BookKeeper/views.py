from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['id', 'bname', 'bcode', 'bprice', 'bauthor', 'bpublisher', 'bedition', 'bstock']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['id', 'aname']

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['id', 'pname']


class BookKeeperForm(ModelForm):
    class Meta:
        model = BookKeeper
        fields = ['id', 'loginname','password','fullname']

class LoginForm(ModelForm):
    class Meta:
        model = BookKeeper
        fields = ['loginname','password']

def dashboard(request, template_name="dashboard.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		data = {"login_status":login_status, "fullname":fullname,"loginname":loginname }
		return render(request, template_name, data)
	else:
		return redirect("BookKeeper:home")

def logout(request):
	#clear the session here...
	request.session['login_status'] = None
	return redirect("BookKeeper:home")

# Create your views here.
def home(request, template_name="home.html"):
	form = LoginForm(request.POST or None)
	if(form.is_valid()):
		loginname = request.POST['loginname']
		password = request.POST['password']
		b = BookKeeper.objects.get(loginname=loginname, password=password)
		#select * from BookKeeper where loginname=loginname and password=password	
		if(b):
			#set the session here...
			request.session['login_status'] = "1"
			request.session['user_fullname'] = b.fullname
			request.session['loginname'] = b.loginname
			
			return redirect("BookKeeper:dashboard")
		else:
			return redirect("BookKeeper:home")
	return render(request, template_name)

def register(request, template_name="register.html"):
	form = BookKeeperForm(request.POST or None)
	if form.is_valid():
		form.save()         #insert int query
		return redirect('BookKeeper:home')
	return render(request, template_name, {"form":form})


def book_list(request, template_name="book_list.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		books = Book.objects.all()    #select * from Book
		data = {}
		data['object_list'] = books
		return render(request, template_name, data)
	else:
		return redirect("BookKeeper:home")

def book_add(request, template_name="book_add.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		form = BookForm(request.POST or None)
		if form.is_valid():
			form.save()         #insert int query
			return redirect('BookKeeper:BookList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")

def book_edit(request, pk, template_name="book_edit.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(Book, pk=pk)	#selct * from books where pk=8
		form = BookForm(request.POST or None, instance=b)
		if form.is_valid():
			form.save()         #update int query
			return redirect('BookKeeper:BookList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")


def book_delete(request, pk):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(Book, pk=pk)	#select * from Book where pk=8
		b.delete()	#delete from Book where ok=8
		return redirect('BookKeeper:BookList')
	else:
		return redirect("BookKeeper:home")

def author_list(request, template_name="author_list.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		author = Author.objects.all()    #select * from Author
		data = {}
		data['object_list'] = author
		return render(request, template_name, data)
	else:
		return redirect("BookKeeper:home")

def author_add(request, template_name="author_add.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		form = AuthorForm(request.POST or None)
		if form.is_valid():
			form.save()         #insert int query
			return redirect('BookKeeper:AuthorList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")

def author_edit(request, pk, template_name="author_edit.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(Author, pk=pk)	#selct * from books where pk=8
		form = AuthorForm(request.POST or None, instance=b)
		if form.is_valid():
			form.save()         #update int query
			return redirect('BookKeeper:AuthorList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")


def author_delete(request, pk):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(Author, pk=pk)	#select * from Author where pk=8
		b.delete()	#delete from Author where ok=8
		return redirect('BookKeeper:AuthorList')
	else:
		return redirect("BookKeeper:home")


def publisher_list(request, template_name="publisher_list.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		author = Publisher.objects.all()    #select * from Publisher
		data = {}
		data['object_list'] = author
		return render(request, template_name, data)
	else:
		return redirect("BookKeeper:home")

def publisher_add(request, template_name="publisher_add.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		form = PublisherForm(request.POST or None)
		if form.is_valid():
			form.save()         #insert int query
			return redirect('BookKeeper:PublisherList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")

def publisher_edit(request, pk, template_name="publisher_edit.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(Publisher, pk=pk)	#selct * from books where pk=8
		form = PublisherForm(request.POST or None, instance=b)
		if form.is_valid():
			form.save()         #update int query
			return redirect('BookKeeper:PublisherList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")


def publisher_delete(request, pk):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(Publisher, pk=pk)	#select * from Publisher where pk=8
		b.delete()	#delete from Publisher where ok=8
		return redirect('BookKeeper:PublisherList')
	else:
		return redirect("BookKeeper:home")


def bookkeeper_list(request, template_name="bookkeeper_list.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		author = BookKeeper.objects.all()    #select * from BookKeeper
		data = {}
		data['object_list'] = author
		return render(request, template_name, data)
	else:
		return redirect("BookKeeper:home")

def bookkeeper_add(request, template_name="bookkeeper_add.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		form = BookKeeperForm(request.POST or None)
		if form.is_valid():
			form.save()         #insert int query
			return redirect('BookKeeper:BookKeeperList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")

def bookkeeper_edit(request, pk, template_name="bookkeeper_edit.html"):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(BookKeeper, pk=pk)	#selct * from books where pk=8
		form = BookKeeperForm(request.POST or None, instance=b)
		if form.is_valid():
			form.save()         #update int query
			return redirect('BookKeeper:BookKeeperList')
		return render(request, template_name, {"form":form})
	else:
		return redirect("BookKeeper:home")


def bookkeeper_delete(request, pk):
	login_status = request.session['login_status']
	fullname = request.session['user_fullname']
	loginname = request.session['loginname']
	if(login_status=="1"):
		b = get_object_or_404(BookKeeper, pk=pk)	#select * from BookKeeper where pk=8
		b.delete()	#delete from BookKeeper where ok=8
		return redirect('BookKeeper:BookKeeperList')
	else:
		return redirect("BookKeeper:home")