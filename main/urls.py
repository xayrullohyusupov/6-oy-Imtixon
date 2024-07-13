from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index_1/',views.index_1,name='index_1'),
    path('index_2/', views.index_2, name='index_2'),
    path('index_3/', views.index_3, name='index_3'),
    path('index_4/', views.index_4, name='index_4'),
    path('index_5/', views.index_5, name='index_5'),
    path('index_6/', views.index_6, name='index_6'),
    path('index_7/', views.index_7, name='index_7'),
    path('about_us/',views.about_us,name='about_us'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('services/',views.services,name='services'),
    path('team/',views.team,name='team'),
    path('portfolio_detail/',views.portfolio_detail,name='portfolio_detail'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('blog/',views.blog,name='blog'),
    path('blog_grid/', views.blog_grid, name='blog_grid'),
    path('blog_listing_left/',views.blog_listing_left,name='blog_listing_left'),
    path('contact/',views.contact,name='contact'),
    path('blog_detail/',views.blog_detail,name='blog_detail'),
    path('index_apps/',views.index_apps,name='index_apps'),
    path('index_cons/',views.index_cons,name='index_cons'),
    path('index_medical/',views.index_medical,name='index_medical'),
    path('index_realest/',views.index_realest,name='index_realest'),
    path('index_education/',views.index_education,name='index_education')

]