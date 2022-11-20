from django.urls import path
from .views import HomePageView, ToursListView, TourDetailsView, AgentListView, AgentDetailsView

urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path("tours/", ToursListView.as_view(), name = "tours"),
    path("tour/<int:pk>/", TourDetailsView.as_view(), name = "tour_details"),
    path("agents/", AgentListView.as_view(), name = "agents"),
    path("agent/<int:pk>/", AgentDetailsView.as_view(), name = "agent_details"),
    
]
