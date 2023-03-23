from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import profileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class ProfilesView(CreateView):
    model = UserProfile
    template_name = 'profiles/create-profile.html'
    fields = '__all__'
    success_url = '/profile'


class UsersView(ListView):
    template_name = 'profiles/users.html'
    model = UserProfile
    context_object_name = 'users'    



# class ProfilesView(View):
#      def get(self, request):
#           form = profileForm()
#           return render(request, 'profiles/create-profile.html',{
#                'form' : form
#           })
     
#      def post(self, request):
#           submitedForm = profileForm(request.POST, request.FILES)
#           if submitedForm.is_valid(): 
#             profile = UserProfile(image = request.FILES['user_image']) 
#             profile.save()
#             return HttpResponseRedirect('/profile')
          
#           return render(request, 'profiles/create-profile.html',{
#                'form' : submitedForm
#           })

