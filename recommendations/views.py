from django.shortcuts import render
from django.http import HttpResponse
from .algo import hybrid_recommendation  # Import your recommendation function
import pandas as pd

def get_recommendations(request):
    if request.method == 'POST':
        keywords = [
            request.POST.get('keyword1', ''),
            request.POST.get('keyword2', ''),
            request.POST.get('keyword3', ''),
            request.POST.get('keyword4', '')
        ]
        user_id = request.POST.get('user_id', '')
        
        recommendations = hybrid_recommendation(user_id, keywords)
        
        context = {
            'recommendations': recommendations.to_dict(orient='records')
        }
        
        return render(request, 'recommendations/result.html', context)
    
    return render(request, 'recommendations/index.html')
