from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponse

from .models import Profile

class HomeView(View):
    """
    Render for the home view of the project.
    """

    template_name='auxiliare/home.html'
    
    def get(self, request):
            
        return render(request, self.template_name)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

installed_apps = getattr(settings, 'INSTALLED_APPS','')
    
class MenuView(View):
    """
    Render for the menu view of the project.
    The menu bar changes according to installed apps
    """

    template_name='menu.html'
    
    def get(self, request):
        
        if 'paperworks' in installed_apps:

            paperworks_menu = True
        
        if 'simplecost' in installed_apps:
            
            simplecost_menu = True
            
        profile = Profile.objects.get(user=request.user)
            
        return render(request, self.template_name, {'paperworks_menu' : paperworks_menu, 'simplecost_menu' : simplecost_menu, 'profile' : profile})
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MenuView, self).dispatch(*args, **kwargs)
    
class MyProfileView(View):
    """
    Render for the user profile view
    """
    
    template_name='accounts/myprofile.html'
    
    def get(self, request,pk):
        """
        If the user requests his profile return it, else return a 403 (Forbidden)
        """    
        requested_profile = Profile.objects.get(user=pk)
        
        if requested_profile.user == self.request.user:
            
            return render(request, self.template_name, {'profile' : requested_profile})
        
        else:
            
            return HttpResponse(status = 403)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyProfileView, self).dispatch(*args, **kwargs)