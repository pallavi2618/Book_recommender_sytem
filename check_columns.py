import pickle
import pandas as pd

# Load the DataFrame
popular_df = pickle.load(open('popular.pkl', 'rb'))

# Print column names
print("DataFrame columns:", popular_df.columns)
