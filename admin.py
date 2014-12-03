from django.contrib import admin
from reviews.models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
	fieldsets=[
		('Title'		     , {'fields': ['title']}),
		('Review information', {'fields': ['review_points', 'review_txt']}),
		('Date information'  , {'fields': ['pub_date'],
								'classes': ['collapse']}),
	]
	list_display = ('title', 'review_points', 'pub_date',  
					'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['title']

admin.site.register(Review, ReviewAdmin)
