from fastapi import FastAPI, APIRouter
from src.components.tweet_replies_service import fetch_reply_tweet_ids_extended

app = FastAPI()
router = APIRouter()

@router.get("/reply")
def get_replies(tweetId: str):
    return {
        "tweetId": tweetId,
        "reply_ids": fetch_reply_tweet_ids_extended(tweetId)
    }

app.include_router(router, prefix="/api/v1")
