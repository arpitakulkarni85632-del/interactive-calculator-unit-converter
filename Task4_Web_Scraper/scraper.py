import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://news.ycombinator.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}


def scrape_headlines():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []

        title_elements = soup.select("span.titleline > a")

        for index, title in enumerate(title_elements[:10], start=1):
            headline = title.get_text(strip=True)
            link = title.get("href", "")

            if link.startswith("item?"):
                link = "https://news.ycombinator.com/" + link

            headlines.append({
                "id": index,
                "headline": headline,
                "url": link
            })

        data = {
            "source": URL,
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_headlines": len(headlines),
            "headlines": headlines
        }

        with open("headlines.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("Web scraping completed successfully!")
        print(f"Total headlines extracted: {len(headlines)}")
        print("Data saved to headlines.json")

        print("\nLatest Technology Headlines:")
        print("-" * 60)

        for item in headlines:
            print(f"{item['id']}. {item['headline']}")
            print(f"   {item['url']}")
            print()

    except requests.exceptions.RequestException as error:
        print("Error while accessing the website:")
        print(error)

    except Exception as error:
        print("An unexpected error occurred:")
        print(error)


if __name__ == "__main__":
    scrape_headlines()
