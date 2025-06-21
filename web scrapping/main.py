import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime

def scrape_freecodecamp():
    url = "https://www.freecodecamp.org/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Fetch the main page
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        print(f"Scraping started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Store all scraped data in a dictionary
        scraped_data = {
            'navigation': [],
            'courses': [],
            'tutorials': [],
            'forum_topics': [],
            'job_resources': [],
            'community_info': {}
        }
        
        # Extract main navigation and structure
        print("Extracting Navigation...")
        nav = soup.find('nav')
        if nav:
            for link in nav.find_all('a'):
                scraped_data['navigation'].append({
                    'text': link.text.strip(),
                    'url': link.get('href', ''),
                    'category': link.get('class', [''])[0]
                })
        
        # Extract learning curriculum
        print("Extracting Courses...")
        curriculum = soup.find_all('div', class_='block-header')
        for block in curriculum:
            course_info = {
                'title': block.find('h2').text.strip() if block.find('h2') else '',
                'description': block.find('p').text.strip() if block.find('p') else '',
                'duration': block.find('span', class_='duration').text.strip() if block.find('span', class_='duration') else '',
                'topics': []
            }
            topics = block.find_next('div', class_='block-body')
            if topics:
                for topic in topics.find_all('a'):
                    course_info['topics'].append({
                        'name': topic.text.strip(),
                        'url': topic.get('href', '')
                    })
            scraped_data['courses'].append(course_info)
        
        # Extract latest tutorials
        print("Extracting Tutorials...")
        tutorials = soup.find_all('article', class_='post')
        for tutorial in tutorials:
            tutorial_info = {
                'title': tutorial.find('h2').text.strip() if tutorial.find('h2') else '',
                'author': tutorial.find('span', class_='author').text.strip() if tutorial.find('span', class_='author') else '',
                'date': tutorial.find('time').text.strip() if tutorial.find('time') else '',
                'url': tutorial.find('a').get('href', '') if tutorial.find('a') else ''
            }
            scraped_data['tutorials'].append(tutorial_info)
        
        # Extract forum hot topics
        print("Extracting Forum Topics...")
        forum_section = soup.find('section', class_='forum-section')
        if forum_section:
            topics = forum_section.find_all('div', class_='topic')
            for topic in topics:
                topic_info = {
                    'title': topic.find('h3').text.strip() if topic.find('h3') else '',
                    'replies': topic.find('span', class_='replies').text.strip() if topic.find('span', class_='replies') else '',
                    'latest_reply': topic.find('time').text.strip() if topic.find('time') else ''
                }
                scraped_data['forum_topics'].append(topic_info)
        
        # Extract job resources
        print("Extracting Job Resources...")
        job_section = soup.find('section', class_='jobs')
        if job_section:
            resources = job_section.find_all('div', class_='resource')
            for resource in resources:
                resource_info = {
                    'title': resource.find('h4').text.strip() if resource.find('h4') else '',
                    'description': resource.find('p').text.strip() if resource.find('p') else '',
                    'link': resource.find('a').get('href', '') if resource.find('a') else ''
                }
                scraped_data['job_resources'].append(resource_info)
        
        # Extract community statistics
        print("Extracting Community Info...")
        stats = soup.find_all('div', class_='stat')
        for stat in stats:
            label = stat.find('div', class_='stat-label')
            number = stat.find('div', class_='stat-number')
            if label and number:
                scraped_data['community_info'][label.text.strip()] = number.text.strip()
        
        # Save the scraped data to a JSON file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'freecodecamp_data_{timestamp}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(scraped_data, f, indent=4, ensure_ascii=False)
        
        print(f"\nScraped data saved to {filename}")
        
        # Print summary
        print("\nScraping Summary:")
        print(f"Navigation Links: {len(scraped_data['navigation'])}")
        print(f"Courses Found: {len(scraped_data['courses'])}")
        print(f"Tutorials Found: {len(scraped_data['tutorials'])}")
        print(f"Forum Topics: {len(scraped_data['forum_topics'])}")
        print(f"Job Resources: {len(scraped_data['job_resources'])}")
        print(f"Community Stats: {len(scraped_data['community_info'])} metrics")
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"Error parsing the webpage: {e}")
        raise  # Re-raise the exception for detailed debugging
    
    print(f"\nScraping completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    scrape_freecodecamp()