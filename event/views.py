from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.shortcuts import  render, redirect
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from event.forms import ContactForm

from event.models import Eventplanner
from authuser.models import CustomUser

from .models import Eventplanner



def index(request):
    eventplanners = Eventplanner.objects.all()[:6]  # Example: Top 5 event planners  # Fetch all Eventplanner objects from the database
    return render(request, 'index.html', {'eventplanners': eventplanners})


def eventplanners(request):
    eventplanners = Eventplanner.objects.all()  # Fetch all Eventplanner objects from the database

    return render(request, 'planners.html', {'eventplanners': eventplanners})



def about(request):
    return render(request, 'about.html')

def defaults(request, event_id):
    # Retrieve the Eventplanner object using the event_id
    eventplanner = get_object_or_404(Eventplanner, id=event_id)
    # Assuming user is authenticated, retrieve user preferences
    # user = request.customuser
     # Collaborative filtering: Recommend events similar to those attended by the user
    # collaborative_events = Event.objects.filter(attendees=user).distinct()

    # Content-based filtering: Recommend events based on location
    # content_based_events = Event.objects.filter(location=user.profile.location)

    # Hybridization: Combine recommendations from both approaches
    # recommended_events = collaborative_events.union(content_based_events)
    # return render(request, 'default.html', {'recommended_events': recommended_events})


    return render(request, 'default.html', {'eventplanner': eventplanner})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a thank you page here
            return redirect('contact')  # Assuming you have a URL named 'contact_success'
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# suggestion
# def recommend_events(request):
#     # Assuming user is authenticated, retrieve user preferences
#     user = request.user

#     # Collaborative filtering: Recommend events similar to those attended by the user
#     collaborative_events = Eventplanner.objects.filter(attendees=user).distinct()

#     # Content-based filtering: Recommend events based on location
#     content_based_events = Eventplanner.objects.filter(location=user.profile.location)

#     # Hybridization: Combine recommendations from both approaches
#     recommended_events = collaborative_events.union(content_based_events)

#     return render(request, 'recommendations.html', {'recommended_events': recommended_events})


# def event_search(request):
#     query = request.GET.get('q')
#     category = request.GET.get('category')

#     # Get all events
#     events = Event.objects.all()

#     # Apply filters if provided
#     if query:
#         events = events.filter(title__icontains=query) | events.filter(description__icontains=query)

#     if category:
#         events = events.filter(categories__name=category)

#     # Get all categories
#     # categories = Category.objects.all()

#     return render(request, 'normal/event_search.html', {'events': events, 'categories': categories})


def search(request):
    query = request.GET.get('q')
    if query:
        # Perform search in both category name and event planner title
        event_planners = Eventplanner.objects.filter(title__icontains=query) | \
                         Eventplanner.objects.filter(planner_categories__category__name__icontains=query)
    else:
        event_planners = Eventplanner.objects.all()
    
    return render(request, 'search_result.html', {'event_planners': event_planners, 'query': query})
