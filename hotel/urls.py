from django.urls import path 
from hotel import views 

app_name = "hotel"

urlpatterns = [
    path("", views.index, name="index"),
    path("about_us", views.about_us, name="about_us"),
    path("detail/<slug:slug>/", views.hotel_detail, name="detail"),
    path("detail/<slug:slug>/room-type/<slug:rt_slug>/", views.room_type_detail, name="room_type_detail"),
    path("selected_rooms/", views.selected_rooms, name="selected_rooms"),
    path("checkout/<booking_id>/", views.checkout, name="checkout"),
    path("invoice/<booking_id>/", views.invoice, name="invoice"),
    path("update_room_status/", views.update_room_status, name="update_room_status"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('reviews/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('faqs/<str:faq_id>/edit/', views.edit_faq, name='edit_faq'),
    path('faqs/<str:faq_id>/delete/', views.delete_faq, name='delete_faq'),
    path('faqs/add/', views.add_faq, name='add_faq'),


    # Payment API
    path('api/checkout-session/<booking_id>/', views.create_checkout_session, name='api_checkout_session'),
    path('success/<booking_id>/', views.payment_success, name='success'),
    path('failed/<booking_id>/', views.payment_failed, name='failed'),
]
