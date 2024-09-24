# Movie Recommendation Scraper

## Overview
This project is a movie data scraper and recommender system that fetches movie titles from Timeout's "Best Movies of All Time" page and retrieves related movie recommendations from the TasteDive API. The results are stored in a CSV file, which includes related movie titles, Wikipedia links, YouTube links, and short descriptions.

The goal of this project is to provide a helpful and valuable resource for movie enthusiasts by offering not only the top films but also related recommendations. This allows users to explore films they might enjoy based on their interests.

## Features
- Scrapes movie titles from Timeout's "Best Movies of All Time."
- Fetches related movie recommendations from the TasteDive API.
- Outputs data into a CSV file (`relatedMovies.csv`) containing:
  - Movie Title
  - Related Movie Title
  - Wikipedia URL
  - YouTube URL
  - Short description of the related movie

## Why This Is Useful
This tool is valuable for anyone looking for quick and reliable movie recommendations. Whether you're a movie critic, casual viewer, or just someone who loves exploring new films, this dataset can help you discover new movies based on what you already like. By using the TasteDive API to get related movies, the CSV file becomes an excellent resource for anyone building their own movie recommendation engine or simply looking for inspiration.

## Setup Instructions

### Prerequisites
Ensure that you have the following tools installed:
- Python 3.x
- `pip` (Python package installer)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/moeez-tariq/relatedMoviesScrape.git
    cd relatedMoviesScrape
    ```

2. Create and activate a virtual environment:
    - On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with your TasteDive API key. The `.env` file should be in the root directory and look like this:
    ```
    TASTEDIVE_API_KEY=your_tastedive_api_key
    ```

5. Run the script:
    ```bash
    python movie_scraper.py
    ```

### Rate Limiting
The TasteDive API has a rate limit, so the script sleeps for 1 second between each request to avoid hitting the limit.

## Potential Use Cases
- **Movie Enthusiasts**: Quickly discover movies related to your favorites.
- **Content Creators**: Use this data for generating content such as movie recommendation lists, blog posts, or YouTube videos.
- **Developers**: Integrate this scraper into a larger project to power movie recommendation engines or personal entertainment apps.


