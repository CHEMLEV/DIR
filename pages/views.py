from django.views.generic import TemplateView, ListView, DetailView
from .models import Tour, Agent

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class ToursListView(ListView):
    model = Tour
    template_name = "tours.html"

class TourDetailsView(DetailView): 
    model = Tour
    template_name = "tour_details.html"

class AgentListView(ListView):
    model = Agent
    template_name = "agents.html"

class AgentDetailsView(DetailView): 
    model = Agent
    template_name = "agent_details.html"
