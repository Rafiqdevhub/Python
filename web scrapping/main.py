import requests
from bs4 import BeautifulSoup
import time

def scrape_freecodecamp():
    url = "https://www.freecodecamp.org/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        print("Successfully retrieved the webpage.\n")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract main navigation links
        print("Main Navigation:")
        nav_items = soup.find_all('a', class_='nav-link')
        for item in nav_items:
            print(f"- {item.text.strip()} -> {item.get('href', '')}")
        
        # Extract certification courses
        print("\nCertification Courses:")
        courses = soup.find_all('div', class_='map-cert-title')
        for course in courses:
            print(f"- {course.text.strip()}")
        
        # Extract recent news/articles
        print("\nRecent Articles:")
        news_items = soup.find_all('a', class_='news-article-link')
        for item in news_items:
            title = item.find('h3')
            if title:
                print(f"- {title.text.strip()}")
                
        # Extract learning platform features
        print("\nPlatform Features:")
        features = soup.find_all('div', class_='feature')
        for feature in features:
            title = feature.find(['h2', 'h3'])
            description = feature.find('p')
            if title and description:
                print(f"- {title.text.strip()}")
                print(f"  {description.text.strip()}\n")
        
        # Extract community stats
        print("\nCommunity Statistics:")
        stats = soup.find_all('div', class_='stat')
        for stat in stats:
            number = stat.find('div', class_='stat-number')
            label = stat.find('div', class_='stat-label')
            if number and label:
                print(f"- {label.text.strip()}: {number.text.strip()}")
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"Error parsing the webpage: {e}")
        
    print("\nScraping completed!")

if __name__ == "__main__":
    scrape_freecodecamp()