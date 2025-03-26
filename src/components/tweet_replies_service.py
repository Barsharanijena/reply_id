import os
import httpx
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
HEADERS = {"Authorization": f"Bearer {BEARER_TOKEN}"}


def fetch_reply_tweet_ids_extended(tweet_id: str):
    meta_url = f"https://api.twitter.com/2/tweets/{tweet_id}?tweet.fields=conversation_id"
    meta_resp = httpx.get(meta_url, headers=HEADERS)

    if meta_resp.status_code != 200:
        raise Exception(f"Failed to fetch tweet metadata: {meta_resp.text}")

    tweet_data = meta_resp.json().get("data")
    if not tweet_data:
        return []

    conversation_id = tweet_data.get("conversation_id")

    search_url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": f"conversation_id:{conversation_id} -is:retweet -is:quote",
        "tweet.fields": "referenced_tweets",
        "max_results": 100
    }

    response = httpx.get(search_url, headers=HEADERS, params=params)

    if response.status_code != 200:
        raise Exception(f"Twitter API error: {response.text}")

    all_tweets = response.json().get("data", [])

    reply_ids = [
        tweet["id"]
        for tweet in all_tweets
        if any(
            ref.get("type") == "replied_to" and ref.get("id") == tweet_id
            for ref in tweet.get("referenced_tweets", [])
        )
    ]

    return reply_ids
