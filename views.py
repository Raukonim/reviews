from django.http import Http404
from django.shortcuts import get_object_or_404, render

from reviews.models import Review

# Create your views here.

def index(request):
	latest_review_list = Review.objects.order_by('-pub_date')
	context = {'latest_review_list': latest_review_list}
	return render(request, 'reviews/index.html', context)
	
def detail(request, review_id):
	review = get_object_or_404(Review, pk=review_id)
	return render(request, 'reviews/detail.html', {'review': review})
