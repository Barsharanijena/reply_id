from src.components.tweet_replies_service import fetch_reply_tweet_ids_extended
from src.logging import logger

if __name__ == "__main__":
    tweet_id = input("Enter Tweet ID to get direct replies: ")
    try:
        replies = fetch_reply_tweet_ids_extended(tweet_id)
        logger.info(f"✅ Fetched {len(replies)} replies to {tweet_id}")
        print(f"\nDirect replies to tweet {tweet_id}:")
        for rid in replies:
            print(f"- {rid}")
    except Exception as e:
        logger.error(f"Error fetching replies for {tweet_id}: {e}")
        print(f"\n❌ Error: {e}")
