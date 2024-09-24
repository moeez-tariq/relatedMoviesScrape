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


# Movie Recommendation Scraper

## Overview
This project is a movie data scraper and recommender system that fetches movie titles from Timeout's "Best Movies of All Time" page and retrieves related movie recommendations from the TasteDive API. The results are stored in a CSV file, which includes related movie titles, Wikipedia links, YouTube links, and short descriptions.

## Data Description

### Scraped Data
- **Source**: Timeout's "Best Movies of All Time" page.
- **Data Gathered**: Movie titles listed as the top films of all time.

### API Data
- **Source**: TasteDive API.
- **Data Gathered**:
  - **Related Movie Titles**: Movies similar to those in Timeout's list.
  - **Wikipedia URLs**: Links to the Wikipedia pages of related movies.
  - **YouTube URLs**: Links to trailers or clips on YouTube.
  - **Short Descriptions**: Brief summaries of related movies.

### Purpose
Timeout's list was chosen because it provides a curated selection of critically acclaimed films that are widely recognized as the greatest in cinema history. By using this list as a starting point, we can ensure that the recommendations are grounded in a widely accepted set of high-quality films. The TasteDive API complements this by suggesting related movies, enhancing the discovery experience with new films that users might enjoy based on their existing favorites.

## Why This Dataset Is Valuable

This dataset offers a comprehensive view of top films and related recommendations, which is not commonly available for free in a consolidated format. Here’s why it’s valuable:

- **Curated List**: Timeout's "Best Movies of All Time" provides a high-quality, curated list of films, ensuring that the recommendations are based on a reputable source.
- **Comprehensive Recommendations**: By including related movie titles, Wikipedia, and YouTube links, users can easily explore new films and learn more about them through accessible resources.
- **Enhanced Discovery**: This dataset supports movie enthusiasts in discovering new films that align with their tastes, enhancing their viewing experience with related suggestions.

### Why This Dataset Might Not Be Publicly Available for Free
Creating such a dataset involves significant effort in scraping data, managing API requests, and aggregating information. Many movie recommendation services either charge for access or integrate the data into proprietary systems, making free, comprehensive datasets rare. This project fills that gap by providing an open resource for movie enthusiasts and developers interested in building or enhancing recommendation engines.

## Features
- Scrapes movie titles from Timeout's "Best Movies of All Time."
- Fetches related movie recommendations from the TasteDive API.
- Outputs data into a CSV file (`relatedMovies.csv`) containing:
  - Movie Title
  - Related Movie Title
  - Wikipedia URL
  - YouTube URL
  - Short description of the related movie

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
