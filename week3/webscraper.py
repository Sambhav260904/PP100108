# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# page=1
# url = 'https://quotes.toscrape.com/page/{}/'

# while True:
#     # response = requests.get('https://quotes.toscrape.com/page/{}/')
#     url = url.format(page)
#     response = requests.get(url)
    
#     print(response)
    
#     # print(response.content)    

#     soup = BeautifulSoup(response.content, 'html.parser')
#     # print(soup.prettify())

#     quotes = soup.find_all('span', class_='text')
#     authors = soup.find_all('small', class_='author')


#     # print(quotes[0].text)
#     # print(authors[0].text)


#     for i in range(len(quotes)):
#         print(authors[i].text+" : "+quotes[i].text)
#         print()
#     page+=1

    



import requests
from bs4 import BeautifulSoup
import csv
import time
import json 


def save_to_csv(data, filename='scraped_data.csv'):
    """Save scraped data to a CSV file."""
    if not data:
        print("No data available to save.")
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data successfully saved to {filename}.")
    
    
def save_to_json(data, filename='scraped_data.json'):
    """Save scraped data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)
    print(f"Data successfully saved to {filename}.")


def main():
    
    # Base URL remains unchanged
    base_url = 'https://quotes.toscrape.com/page/{}/'
    page = 1
    scraped_data=[]

    while True:
        # Generate URL for the current page
        url = base_url.format(page)
        response = requests.get(url, timeout=10)
        
        # Check if the page exists
        if response.status_code != 200:
            print(f"Page {page} returned status code {response.status_code}. Stopping the scraper.")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract quotes and authors
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        
        # If no quotes are found, assume it's the end of the pages
        if not quotes:
            print("No quotes found on page. End of pages reached.")
            break

        # Process and print the quotes and authors
        for i in range(len(quotes)):
            
             scraped_data.append({
                'author': authors[i].text,
                'quote': quotes[i].text
            })
            # print(f"{authors[i].text} : {quotes[i].text}\n")
        
        page += 1
        # Optional: pause briefly between page requests
        time.sleep(1)

    file_format = input("Enter the file format to save (csv/json): ").lower()
    if file_format == 'csv':
        save_to_csv(scraped_data)
    elif file_format == 'json':
        save_to_json(scraped_data)
    else:
        print("Invalid format specified. Data not saved.")
    


if __name__=="__main__":
    main()























