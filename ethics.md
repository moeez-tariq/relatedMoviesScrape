# Ethics and Data Usage

## Overview
This project scrapes publicly available movie titles from Timeout's "Best Movies of All Time" page and uses the TasteDive API to retrieve related movie recommendations. The primary objective is to provide movie enthusiasts and developers with a dataset that offers valuable recommendations based on popular films. 

This project is strictly for educational purposes and does not store or manipulate any personal data. The data collected consists solely of publicly available movie titles, metadata, and related movie suggestions.

## Compliance with `robots.txt`
In accordance with the `robots.txt` file from Timeout.com, this project ensures that it adheres to the guidelines provided by the site. The `robots.txt` file explicitly disallows crawling specific endpoints, which are primarily related to user accounts, search functionality, and other protected pages. This project does not attempt to scrape any of the disallowed paths or restricted content.

The scraping process is limited to accessing publicly available pages, specifically the movie titles listed on the "Best Movies of All Time" page, which is not restricted by the site's `robots.txt`.

### Timeout.com `robots.txt` Key Guidelines:
- **Disallowed Sections**: The project respects all disallow directives, avoiding any restricted URLs related to user accounts, search, or dynamic content.
- **Allowed Sections**: The specific page containing the list of top movies is not restricted by the `robots.txt`, allowing this project to ethically and legally scrape the movie titles.

## Use of Public Data Only
- The project does not involve the collection of any personal data.
- All the data obtained from the Timeout.com website consists of publicly accessible movie titles.
- Movie-related data fetched from the TasteDive API is also publicly available and meant for use by developers.

## Educational Purpose
This project has been developed as an educational tool to demonstrate web scraping and API integration techniques. The output generated (i.e., related movie recommendations) serves as a valuable resource for:
- Learning and experimenting with data scraping and API usage.
- Building datasets for personal movie recommendation systems.
- Exploring how movie data can be enriched with external APIs like TasteDive.

## Avoiding Overload and Rate Limits
The project includes API Rate Limiting mechanisms to avoid excessive requests and follows best practices for web scraping to minimize the impact on the source servers.