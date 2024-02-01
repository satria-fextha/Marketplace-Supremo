from django.urls import path
from . import views

urlpatterns = [
    # URL for submitting a new rating and review
    path('ratings/', views.RatingCreateView.as_view(), name='rating_create'),
    # URL for moderating and approving reviews
    path('reviews/moderate/', views.ReviewModerateView.as_view(), name='review_moderate'),
]
