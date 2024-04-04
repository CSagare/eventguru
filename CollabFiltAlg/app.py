from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load event_titles_map from event_titles.txt
event_titles_map = {}
with open('event_titles.txt') as f:
    for line in f.readlines():
        parts = [x.strip() for x in line.split(',')]
        event_id = int(parts[0])
        event_name = parts[1]
        event_titles_map[event_id] = event_name

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    # Get user input from the form
    active_client = int(request.form['client_id'])
    K = int(request.form['k'])

    # Get recommendations from the model
    # recommended_events = model[active_client][:K]
      # Check if the active_client exists in the model
    if active_client in model:
        recommended_events = model[active_client][:K]
    else:
        # Handle the case where active_client is not in the model
        recommended_events = []

    # Render the recommendations template with the recommended events
    return render_template('recommendations.html', recommended_events=recommended_events, event_titles_map=event_titles_map)

if __name__ == '__main__':
    app.run(debug=True)



# Assuming you have implemented content-based recommendations function and have event data
def content_based_recommendation(active_client, K):
    # Implementation of content-based recommendation function
    pass

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/content_recommendations', methods=['POST'])
def content_recommendations():
    active_client = int(request.form['client_id'])
    K = int(request.form['k'])
    
    # Call content-based recommendation function to get recommendations for the active client
    recommendations = content_based_recommendation(active_client, K)
    
    # Render the template with the recommended events
    return render_template('content.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
