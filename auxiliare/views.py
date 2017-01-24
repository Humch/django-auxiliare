from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View

class HomeView(View):
    
    template_name='auxiliare/home.html'
    
    def get(self, request):
        """
        Get method for the home view of the project.
        Modify menu according to installed apps
        """
        
        if 'paperworks' in settings.INSTALLED_APPS:
            paperworks = True
        else:
            paperworks = False
        
        if 'shoppinglist' in settings.INSTALLED_APPS:
            shopping_list = True
        else:
            shopping_list = False
            
        return render(request, self.template_name,{'paperworks':paperworks,'shopping_list':shopping_list})
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
