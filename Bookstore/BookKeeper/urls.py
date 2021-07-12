from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from BookKeeper import views

urlpatterns = [
    	url(r'^$', views.home, name='home'),
        url(r'register/', views.register, name='register'),
        url(r'dashboard/', views.dashboard, name='dashboard'),
        url(r'logout/', views.logout, name='logout'),
    	
    	#url patterns for Book
    	url(r'BookList/', views.book_list, name='BookList'),
    	url(r'BookAdd/', views.book_add, name='BookAdd'),
    	url(r'BookEdit/(?P<pk>\d+)$', views.book_edit, name='BookEdit'),
    	url(r'BookDelete/(?P<pk>\d+)$', views.book_delete, name='BookDelete'),

    	#url patterns for Author
    	url(r'AuthorList/', views.author_list, name='AuthorList'),
    	url(r'AuthorAdd/', views.author_add, name='AuthorAdd'),
    	url(r'AuthorEdit/(?P<pk>\d+)$', views.author_edit, name='AuthorEdit'),
    	url(r'AuthorDelete/(?P<pk>\d+)$', views.author_delete, name='AuthorDelete'),

        #url patterns for Publisher
        url(r'PublisherList/', views.publisher_list, name='PublisherList'),
        url(r'PublisherAdd/', views.publisher_add, name='PublisherAdd'),
        url(r'PublisherEdit/(?P<pk>\d+)$', views.publisher_edit, name='PublisherEdit'),
        url(r'PublisherDelete/(?P<pk>\d+)$', views.publisher_delete, name='PublisherDelete'),

        #url patterns for BookKeeper
        url(r'BookKeeperList/', views.bookkeeper_list, name='BookKeeperList'),
        url(r'BookKeeperAdd/', views.bookkeeper_add, name='BookKeeperAdd'),
        url(r'BookKeeperEdit/(?P<pk>\d+)$', views.bookkeeper_edit, name='BookKeeperEdit'),
        url(r'BookKeeperDelete/(?P<pk>\d+)$', views.bookkeeper_delete, name='BookKeeperDelete'),

]