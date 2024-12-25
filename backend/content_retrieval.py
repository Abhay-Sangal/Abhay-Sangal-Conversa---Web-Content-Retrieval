import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_web_content(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Send request to Google search page
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Google search results: {e}")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract URLs from search results
    links = [a['href'] for a in soup.select('a[href^="http"]')]

    text_content = ""
    for link in links[:3]:  # Retrieve content from top 3 links
        try:
            # Ensure full URL if the link is relative
            full_link = urljoin(search_url, link)
            page_response = requests.get(full_link, headers=headers)
            page_response.raise_for_status()  # Check if page request is successful

            page_soup = BeautifulSoup(page_response.content, "html.parser")
            paragraphs = page_soup.find_all("p")
            page_text = " ".join([para.get_text() for para in paragraphs])

            text_content += page_text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from {link}: {e}")
            continue  # Skip any URL that raises an error

    return text_content
