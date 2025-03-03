#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys
import time
import json
import csv

def scrape_google_scholar(query, num_results=100):
    results = []
    start = 0
    headers = {
        "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/108.0.0.0 Safari/537.36")
    }
    print(f"scraping google scholar.. attempting {num_results}")
    while len(results) < num_results:
        url = f"https://scholar.google.com/scholar?hl=en&q={query}&start={start}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching page: HTTP {response.status_code}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        entries = soup.select('.gs_r.gs_or.gs_scl')
        if not entries:
            print("No more results found.")
            break
        
        for entry in entries:
            # Extract title and link
            title_elem = entry.select_one('.gs_rt')
            title = title_elem.get_text() if title_elem else "N/A"
            link = title_elem.find('a')['href'] if title_elem and title_elem.find('a') else "N/A"
            # Extract authors and metadata
            author_elem = entry.select_one('.gs_a')
            authors = author_elem.get_text() if author_elem else "N/A"
            
            results.append({
                "title": title,
                "link": link,
                "authors": authors
            })
            if len(results) >= num_results:
                break
        
        start += 10
        time.sleep(2)  # Delay to prevent potential rate limiting
    print(f"{len(results)} results sracped")
    return results

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 scholar_scraper.py 'search query' output.csv")
        sys.exit(1)
    
    query = sys.argv[1]
    csv_filename = sys.argv[2]
    results = scrape_google_scholar(query)
    #print(json.dumps(results, indent=2))

    with open(csv_filename, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["title", "link", "authors"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"results aved to {csv_filename}")
