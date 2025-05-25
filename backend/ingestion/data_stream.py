import time
from ingestion.news_fetcher import fetch_news_from_exa
from config.subscriptions import get_subscribed_topics

def stream_articles(domain="general", delay=10):
    seen = set()
    while True:
        articles = fetch_news_from_exa(domain=domain)
        for article in articles:
            if article["url"] not in seen:
                seen.add(article["url"])

                # 🔔 Alert on matching subscribed topics
                for topic in get_subscribed_topics("default_user"):
                    if topic in article["title"].lower() or topic in article["content"].lower():
                        print(f"🔔 ALERT: New article for topic '{topic}': {article['title']}")
                
                yield article

        time.sleep(delay)
