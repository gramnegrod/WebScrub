import json
import os

# File path relative to the current script file for the external text data
script_directory = os.path.dirname(__file__)
data_file_path = os.path.join(script_directory, 'news.txt')  # Using news.txt as the data file

# Function to read JSON data from a text file
def read_json_from_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.loads(file.read())

# Read data
try:
    news_narratives = read_json_from_text_file(data_file_path)
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error reading the text file: {e}")

# Your processing logic here (e.g., saving data to another file, processing data, etc.)
