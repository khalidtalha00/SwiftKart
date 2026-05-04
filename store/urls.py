from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('login/', views.login_view, name="login"),
	path('logout/', views.logout_view, name="logout"),
	path('register/', views.register, name="register"),
	path('cart/', views.cart, name="cart"),
	path('profile/', views.profile, name="profile"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]