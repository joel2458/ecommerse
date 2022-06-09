from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('load_user_signup',views.load_user_signup,name='load_user_signup'),
    path('load_user_login',views.load_user_login,name='load_user_login'),
    path('load_user_home',views.load_user_home,name='load_user_home'),
    path('show_profile',views.show_profile,name='show_profile'),
    path('user_edit_profile',views.user_edit_profile,name='user_edit_profile'),


    path('load_admin_home',views.load_admin_home,name='load_admin_home'),
    path('load_add_category',views.load_add_category,name='load_add_category'),
    path('add_category',views.add_category,name='add_category'),
    
    path('add_product',views.add_product,name='add_product'),
    path('load_admin_add_product',views.load_admin_add_product,name='load_admin_add_product'),
    path('load_admin_show_product',views.load_admin_show_product,name='load_admin_show_product'),
    path('admin_show_product',views.admin_show_product,name='admin_show_product'),
    path('admin_delete_product/<int:pk>',views.admin_delete_product,name='admin_delete_product'),
    path('load_admin_edit_product/<int:pk>',views.load_admin_edit_product,name='load_admin_edit_product'),
    path('admin_edit_product/<int:pk>',views.admin_edit_product,name='admin_edit_product'),
    path('show_user_details',views.show_user_details,name='show_user_details'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),
    # path('load_product_details',views.load_product_details,name='load_product_details'),
    #path('product_multiimage/<int:pk>',views.product_multiimage,name='product_multiimage'),
    # path('load_add_mul',views.add_mul_img,name='add_mul_img'),
    
    # path('addimg',views.addimg,name='addimg'),
    #path('add_mulimg',views.add_mulimg,name='add_mulimg'),
    #path('addimage',views.addimage,name='addimage'),
    path('showimage/<int:pk>',views.showimage,name='showimage'),
    #path('add_mul',views.add_mul,name='add_mul'),
    # path('load_admin_add_mul',views.load_admin_add_mul,name='load_admin_add_mul'),
    # path('add_to_cart_view/<int:pk>', views.add_to_cart_view,name='add_to_cart_view'),
    # path('cart_view', views.cart_view,name='cartview'),
    # path('remove_from_cart_view/<int:pk>', views.remove_from_cart_view,name='remove_from_cart_view'),
    # path('cart',views.cart,name='cart'),
    path('load_mul',views.load_mul,name='load_mul'),
    path('add_mul_img',views.add_mul_img,name='add_mul_img'),


    path('about',views.about,name='about'),
    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('detail/<int:pk>',views.detail,name='detail'),
    
    # path('checkout',views.checkout,name='checkout'),
    
    
    path('user_signup',views.user_signup,name='user_signup'),
    path('user_login',views.user_login,name='user_login'),
    path('logout',views.logout,name='logout'),
    path('user_show_product',views.user_show_product,name='user_show_product'),

]