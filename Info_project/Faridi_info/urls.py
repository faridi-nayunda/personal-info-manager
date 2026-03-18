from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name="my_view"),
    path('create/', views.create_page_view, name="create_page"),
    path('success/', views.success_page_view, name="info_page"),
    path('update/<int:id>/', views.update_info_page, name="update_info"),
    path('delete/<int:id>/', views.delete_info_page, name="delete_info"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('protected/', views.ProtectedView.as_view(), name="protected"),
   
]
