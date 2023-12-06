import os
import requests

# Get the API key from the environment variable
API_KEY = os.environ.get('NEWSAPI')

# Check if the API key is available
if API_KEY is None:
    print("API key not found. Please set the 'NEWSAPI' environment variable.")
else:
    url = f'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={API_KEY}'

    try:
        # Send the GET request with a timeout of 10 seconds
        response = requests.get(url, timeout=10)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            content = response.json()

            # Extract and print all titles
            articles = content['articles']
            for article in articles:
                title = article['title']
                print(title)

        else:
            print(f"Error: Unable to fetch content. Status code: {response.status_code}")

    except requests.Timeout:
        print("Error: Request timed out. Please check your internet connection.")
    except requests.RequestException as e:
        print(f"Error: {e}")

