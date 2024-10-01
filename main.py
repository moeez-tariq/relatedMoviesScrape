import requests
from bs4 import BeautifulSoup
import re
import csv
from dotenv import load_dotenv
import os
from urllib.parse import quote
import time

# Function to get related movies from TasteDive
def get_related_movies(title):
    try:
        params = {
            'k': api_key,
            'q': f"{title}",
            'type': 'movie',
            'info': 1
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an error for non-200 status codes

        data = response.json()
        if 'similar' in data and 'results' in data['similar']:
            return data['similar']['results']
        else:
            print(f"Unexpected response structure for movie: {title}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Request failed for movie '{title}': {e}")
        return []
    except ValueError as e:
        print(f"Error parsing JSON response for movie '{title}': {e}")
        return []


# Load environment variables from .env file
load_dotenv()

# Get the TasteDive API key from environment variables
api_key = os.getenv('TASTEDIVE_API_KEY')
if not api_key:
    raise ValueError("API key not found in environment variables. Make sure it's set correctly.")

# Base URL for the TasteDive API
base_url = 'https://tastedive.com/api/similar'

# URL of the Timeout best movies page
url = "https://www.timeout.com/film/best-movies-of-all-time"

# Send a GET request to the website
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for non-200 status codes
except requests.exceptions.RequestException as e:
    raise SystemExit(f"Failed to fetch the URL: {url}. Error: {e}")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all movie title containers
title_containers = soup.find_all('h3', class_='_h3_cuogz_1')

# Create a list to store the movie titles
movie_titles = []

# Define a regex pattern to remove the year in parentheses
pattern = re.compile(r'\s*\(\d{4}\)$')

# Iterate over the title containers and extract titles
for container in title_containers:
    try:
        # Remove the <span> tag from the title text
        span = container.find('span')
        if span:
            span.decompose()  # Remove the <span> tag from the tree
        # Get the text without leading/trailing spaces
        title = container.text.strip()
        # Remove the year in parentheses
        title = pattern.sub('', title)
        # Append the cleaned title to the list
        movie_titles.append(title)
    except AttributeError as e:
        print(f"Error parsing movie title container: {e}")


# Create or open the CSV file for writing
with open('relatedMovies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Movie Title', 'Related Movie Title', 'Wikipedia URL', 'YouTube URL', 'Description'])

    # Iterate over movies and write data to CSV
    for movie in movie_titles:
        all_related = get_related_movies(movie)
        
        if len(all_related) == 0:
            print(f"No related movies found for '{movie}'.")
            continue

        # Go through all the related movies and add a row for each to the csv file
        for related in all_related:
            title = related.get('name', '')
            wUrl = related.get('wUrl', '')
            yUrl = related.get('yUrl', '')
            description = related.get('description', '')
            
            # Write movie data to the CSV file
            writer.writerow([movie, title, wUrl, yUrl, description])
        time.sleep(1) # Sleep for 1 second to avoid hitting the API rate limit

print("Movie data has been saved.")
