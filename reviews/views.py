from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewFrom
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

class ReviewView(CreateView):
    model = Review
    form_class = ReviewFrom
    template_name = 'reviews/review.html'
    success_url = 'thank-you/'

# class ReviewView(FormView):
#     form_class = ReviewFrom
#     template_name = 'reviews/review.html'
#     success_url = 'thank-you/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#    def get(self, request):
#         form = ReviewFrom()
#         return render(request,'reviews/review.html',{
#             'form': form 
#         })

#    def post(self, request):
#         form = ReviewFrom(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('thank-you/')
        
#         return render(request,'reviews/review.html',{
#             'form': form 
#         })
   

class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) 
        context['massage'] = 'thats work!'
        return context  


# class ReviewListView(TemplateView):
#     template_name = 'reviews/review-list.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context

class ReviewListView(ListView):
    template_name = 'reviews/review-list.html'
    model = Review
    context_object_name = 'reviews'

    # for filter data

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
        

 
class ReviewDetailView(DetailView):
    template_name = 'reviews/review-detail.html'
    model = Review
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session['favorite_review']
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context

        
    


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review-id']
        # fav_review = Review.objects.get(pk=review_id) # save object in session and JSON error
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/'+ review_id)
    
# class ReviewDetailView(TemplateView):
#     template_name = 'reviews/review-detail.html'
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         id_review = kwargs['id']
#         review = Review.objects.get(pk=id_review)
#         context['review'] = review  
#         return context

# class ThankYouView(View):
#     def get(self, request):
#      return render (request,'reviews/thank-you.html')


#method base views

# def review(request):
#    if request.method == 'POST':
#       form = ReviewFrom(request.POST)

#       if form.is_valid():
#         # review = Review(user_name=form.cleaned_data['user_name'],
#         #                 text_review=form.cleaned_data['feedback'],
#         #                 rating=form.cleaned_data['rating'])
#         # review.save() 
#         form.save()
#         print(form.cleaned_data)
#         return HttpResponseRedirect('thank-you/')
#    else:  
#        form = ReviewFrom()
#    return render(request,'reviews/review.html',{
#       'form': form
#    })


# def Thank_you(request):
#    return render(request,'reviews/thank-you.html')