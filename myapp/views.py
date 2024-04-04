from django.shortcuts import render
from .utils import load_pickled_data


def get_recommendations(request):
    # Load pickled data
    data = load_pickled_data()

    # Extract required data
    users_df = data['users_df']
    events_df = data['events_df']
    interactions_df = data['interactions_df']
    tfidf_matrix = data['tfidf_matrix']

    # Your recommendation logic here
    # For example, using content-based filtering
    user_preferences_content = f"{user_location} {user_price} {user_services}"  # Replace with actual user preferences
    recommended_events_content = get_recommendations_content(user_preferences_content, tfidf_matrix, events_df)

    # Combine with collaborative filtering
    # For demonstration, using a placeholder function for collaborative filtering
    recommended_events_collab = collaborative_filtering(users_df, events_df)
    
    # Combine recommendations
    hybrid_recommendations = pd.concat([recommended_events_content, recommended_events_collab]).drop_duplicates().reset_index(drop=True)

    # Convert recommendations to a format suitable for rendering
    recommendations = hybrid_recommendations[['event_id', 'rating', 'planners']].to_dict(orient='records')

    return render(request, 'recommendations.html', {'recommendations': recommendations})
