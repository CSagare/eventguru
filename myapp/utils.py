import pickle

def load_pickled_data(file_path='myapp/recommendations.pkl'):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data
