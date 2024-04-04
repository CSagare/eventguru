# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from surprise import Dataset, Reader, KNNBasic

# # Assuming you have the following DataFrames loaded:
# # events_df, users_df
# events_df = pd.read_csv('recommendations/events.csv')
# users_df = pd.read_csv('recommendations/users.csv')
# events_df = events_df.dropna()  # Drop rows with any missing values
# users_df = users_df.dropna()  # Drop rows with any missing values

# # Merge events and users on 'user_id'
# users_df = users_df.merge(events_df, on='user_id')
# users_df = users_df.dropna()  # Drop rows with any missing values

# C = users_df['rating'].mean()
# m = users_df['vote_count'].quantile(0.9)

# q_movies = users_df.copy().loc[users_df['vote_count'] >= m]

# def weighted_rating(x, m=m, C=C):
#     v = x['vote_count']
#     R = x['rating']
#     return (v/(v+m) * R) + (m/(m+v) * C)

# q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
# q_movies = q_movies.sort_values('score', ascending=False)

# pop = events_df.sort_values('popularity', ascending=False)

# # Initialize TF-IDF Vectorizer
# tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix = tfidf_vectorizer.fit_transform(events_df['planners'] + ' ' + events_df['location'] + ' ' + events_df['price'])
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# # Load data for Surprise
# reader = Reader(rating_scale=(1, 5))
# data = Dataset.load_from_df(users_df[['user_id', 'event_id', 'rating']], reader)
# trainset = data.build_full_trainset()

# sim_options = {'name': 'cosine', 'user_based': True}
# model = KNNBasic(sim_options=sim_options)
# model.fit(trainset)




# def collaborative_filtering_recommendation(user_id, model=model):
#     all_event_ids = events_df['event_id'].unique()
#     predictions = [model.predict(user_id, event_id) for event_id in all_event_ids]
    
#     estimated_ratings = [pred.est for pred in predictions]
    
#     collab_df = pd.DataFrame({
#         'event_id': all_event_ids,
#         'rating_collab': estimated_ratings
#     })
    
#     sorted_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)
#     top_n = sorted_predictions[:10]
    
#     recommended_event_ids = [pred.iid for pred in top_n]
    
#     return events_df[events_df['event_id'].isin(recommended_event_ids)][['event_id', 'planners', 'location', 'price', 'rating']], collab_df

# def content_based_recommendation(user_id, keywords, cosine_sim=cosine_sim):
#     # Fetch rated event ids for the user
#     rated_event_ids = users_df[users_df['user_id'] == user_id]['event_id'].tolist()
    
#     if not rated_event_ids:
#         return pd.DataFrame()
    
#     event_id_to_index = {event_id: index for index, event_id in enumerate(events_df['event_id'])}
#     last_rated_event_index = event_id_to_index.get(rated_event_ids[-1])
    
#     if last_rated_event_index is None:
#         return pd.DataFrame()
    
#     sim_scores = list(enumerate(cosine_sim[last_rated_event_index]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:10] if len(sim_scores) > 1 else sim_scores
    
#     event_indices = [i[0] for i in sim_scores]
#     similar_events = events_df.iloc[event_indices][['event_id', 'planners', 'location', 'price', 'rating','services']]
    
#     return similar_events

# def hybrid_recommendation(user_id, keywords):
#     if len(keywords) != 4:
#         print("Please provide exactly 4 keywords for the search.")
#         return pd.DataFrame()
    
#     # Filter events based on keywords
#     keyword_search_results = events_df[events_df.apply(
#         lambda row: all(keyword.lower() in ' '.join(row.astype(str)).lower() for keyword in keywords if keyword) , axis=1)]
    
#     content_based_rec = content_based_recommendation(user_id, keywords)
#     collaborative_filtering_rec, collab_df = collaborative_filtering_recommendation(user_id)

    
#     print("Columns of content_based_rec:", content_based_rec.columns)
#     print("Columns of collaborative_filtering_rec:", collaborative_filtering_rec.columns)
    
    
#     hybrid_rec = pd.merge(content_based_rec, collaborative_filtering_rec, on='event_id', how='outer', suffixes=('', '_collab'))
#     hybrid_rec.dropna(subset=['planners', 'location', 'price', 'rating'], inplace=True)
    
#     similar_events = hybrid_rec[hybrid_rec['event_id'].isin(keyword_search_results['event_id'].tolist())].copy()  # Explicitly create a copy
    
#     similar_events.loc[:, 'weighted_score'] = 0.7 * similar_events['rating'] + 0.3 * similar_events['rating_collab']
    
#     vote_counts = users_df.groupby('event_id')['rating'].count().reset_index()
#     vote_counts.columns = ['event_id', 'vote_count']
    
#     similar_events = pd.merge(similar_events, vote_counts, on='event_id', how='left')
    
#     similar_events = similar_events.sort_values(by=['weighted_score', 'vote_count'], ascending=[False, False])
    
#     similar_events['rank'] = range(1, len(similar_events) + 1)
    
#     similar_events = similar_events.head(10)
    
#     return similar_events[['rank', 'event_id', 'planners', 'location', 'price', 'rating', 'services', 'vote_count']]


# # Example usage
# # user_id = 3647864012
# # keywords = ['', '', '', '']

# # recommendations = hybrid_recommendation(user_id, keywords)
# # print("Hybrid Recommendations:")
# # print(recommendations)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader, KNNBasic

# Assuming you have the following DataFrames loaded:
# events_df, users_df
events_df = pd.read_csv('recommendations/events.csv')
users_df = pd.read_csv('recommendations/users.csv')
events_df = events_df.dropna()  # Drop rows with any missing values
users_df = users_df.dropna()  # Drop rows with any missing values

# Merge events and users on 'user_id'
users_df = users_df.merge(events_df, on='user_id')
users_df = users_df.dropna()  # Drop rows with any missing values

C = users_df['rating'].mean()
m = users_df['vote_count'].quantile(0.9)

q_movies = users_df.copy().loc[users_df['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['rating']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

pop = events_df.sort_values('popularity', ascending=False)

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(events_df['planners'] + ' ' + events_df['location'] + ' ' + events_df['price'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Load data for Surprise
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(users_df[['user_id', 'event_id', 'rating']], reader)
trainset = data.build_full_trainset()

sim_options = {'name': 'cosine', 'user_based': True}
model = KNNBasic(sim_options=sim_options)
model.fit(trainset)

def collaborative_filtering_recommendation(user_id, model=model):
    all_event_ids = events_df['event_id'].unique()
    predictions = [model.predict(user_id, event_id) for event_id in all_event_ids]
    
    estimated_ratings = [pred.est for pred in predictions]
    
    collab_df = pd.DataFrame({
        'event_id': all_event_ids,
        'rating_collab': estimated_ratings
    })
    
    sorted_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)
    top_n = sorted_predictions[:10]
    
    recommended_event_ids = [pred.iid for pred in top_n]
    
    print("Recommended Event IDs:", recommended_event_ids)  # Debug print
    
    if 'event_id' not in events_df.columns:
        print("event_id column not found in events_df")  # Debug print
        return pd.DataFrame()
    
    return events_df[events_df.event_id.isin(recommended_event_ids)][['event_id', 'planners', 'location', 'price', 'rating']]

def content_based_recommendation(user_id, keywords, cosine_sim=cosine_sim):
    # Fetch rated event ids for the user
    rated_event_ids = users_df[users_df['user_id'] == user_id]['event_id'].tolist()
    
    if not rated_event_ids:
        return pd.DataFrame()
    
    event_id_to_index = {event_id: index for index, event_id in enumerate(events_df['event_id'])}
    last_rated_event_index = event_id_to_index.get(rated_event_ids[-1])
    
    if last_rated_event_index is None:
        return pd.DataFrame()
    
    sim_scores = list(enumerate(cosine_sim[last_rated_event_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:10] if len(sim_scores) > 1 else sim_scores
    
    event_indices = [i[0] for i in sim_scores]
    similar_events = events_df.iloc[event_indices][['event_id', 'planners', 'location', 'price', 'rating','services']]
    
    return similar_events

def hybrid_recommendation(user_id, keywords):
    if len(keywords) != 4:
        print("Please provide exactly 4 keywords for the search.")
        return pd.DataFrame()
    
    # Filter events based on keywords
    keyword_search_results = events_df[events_df.apply(
        lambda row: all(keyword.lower() in ' '.join(row.astype(str)).lower() for keyword in keywords if keyword) , axis=1)]
    
    content_based_rec = content_based_recommendation(user_id, keywords)
    collaborative_filtering_rec = collaborative_filtering_recommendation(user_id)

    print("Columns of content_based_rec:", content_based_rec.columns)
    print("Columns of collaborative_filtering_rec:", collaborative_filtering_rec.columns)
    
    hybrid_rec = pd.merge(content_based_rec, collaborative_filtering_rec, on='event_id', how='outer', suffixes=('', '_collab'))
    hybrid_rec.dropna(subset=['planners', 'location', 'price', 'rating'], inplace=True)
    
    similar_events = hybrid_rec[hybrid_rec['event_id'].isin(keyword_search_results['event_id'].tolist())].copy()  # Explicitly create a copy
    
    similar_events.loc[:, 'weighted_score'] = 0.7 * similar_events['rating'] + 0.3 * similar_events['rating_collab']
    
    vote_counts = users_df.groupby('event_id')['rating'].count().reset_index()
    vote_counts.columns = ['event_id', 'vote_count']
    
    similar_events = pd.merge(similar_events, vote_counts, on='event_id', how='left')
    
    similar_events = similar_events.sort_values(by=['weighted_score', 'vote_count'], ascending=[False, False])
    
    similar_events['rank'] = range(1, len(similar_events) + 1)
    
    similar_events = similar_events.head(10)
    
    return similar_events[['rank', 'event_id', 'planners', 'location', 'price', 'rating', 'services', 'vote_count']]

# Example usage
# user_id = 3647864012
# keywords = ['', '', '', '']

# recommendations = hybrid_recommendation(user_id, keywords)
# print("Hybrid Recommendations:")
# print(recommendations)
