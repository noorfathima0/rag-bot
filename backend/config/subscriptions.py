# backend/config/subscriptions.py

# In-memory subscription store
subscriptions = {}

def add_subscription(user_id: str, topic: str):
    topic = topic.lower().strip()
    subscriptions.setdefault(user_id, set()).add(topic)

def get_subscribed_topics(user_id: str):
    return subscriptions.get(user_id, set())
