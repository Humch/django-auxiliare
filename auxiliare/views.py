from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View

class HomeView(View):
    """
    Render for the home view of the project.
    Modify menu according to installed apps
    """

    template_name='auxiliare/home.html'
    
    def get(self, request):
            
        return render(request, self.template_name)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
