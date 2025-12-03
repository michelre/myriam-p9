from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

# Create your views here.
# Feed view
class FeedPageView(LoginRequiredMixin, View):
    template_name = 'feed.html'
    login_url = 'authentication:login'

    def get(self, request):
        tickets = Tickets.objects.all()

        return render(request, self.template_name, context={'tickets': tickets})
