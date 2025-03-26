# 🐦 Tweet Replies Fetcher

A Python-based microservice to fetch **direct replies** to a given tweet using **Twitter API v2**.  
It supports both a **FastAPI REST API** and a **command-line runner**. Ideal for building reply-thread visualizers, conversation trees, or Twitter data analysis tools.

---

## ✨ Features

- 📌 Fetch direct replies to any tweet using the tweet ID
- 🧠 Automatically resolves `conversation_id` and filters replies
- 🔍 Twitter API v2 based search query logic
- 🛠️ CLI support for manual testing (`app.py`)
- 🌐 FastAPI route with Swagger documentation
- 🪵 Built-in logging with timestamped log files

---

## 🧱 Prerequisites

- Python 3.10+
- Twitter Developer Account & Bearer Token (v2 API)
- `.env` file containing credentials

---

## 📁 Project Structure

```bash
reply_tweet_id/
├── app.py                                  
├── .env                                    
├── requirements.txt                         
│
├── api/
│   └── twitter_replies_service_api.py      
│
├── src/
│   ├── components/
│   │   └── tweet_replies_service.py         
│   └── logging/
│       └── __init__.py                    
│
└── logs/                                   
⚙️ Setup & Installation
🔧 Clone the repository:

git clone https://github.com/Sudibya/tweet_replies_fetcher.git
cd tweet_replies_fetcher
🛠️ Create and activate a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
📦 Install the dependencies:

pip install -r requirements.txt
🔐 Set up .env file:
Create a .env file in the root directory and add your credentials:


BEARER_TOKEN=your_twitter_bearer_token
🚀 Usage
▶️ Manual Mode (CLI)
To run the script manually via terminal:


python app.py
You'll be prompted to enter a tweet ID, and the system will fetch all direct replies to that tweet.

🌐 API Mode (FastAPI)
To run the API server:


uvicorn api.twitter_replies_service_api:app --reload
Then go to:
http://127.0.0.1:8000/docs
and test the /reply endpoint with your desired tweet ID.

📥 Sample API Request
http

GET /reply?tweetId=1904241448054317284
✅ Example Response
json

{
  "tweetId": "1904241448054317284",
  "reply_ids": [
    "1904242235980572832",
    "1904243157085046784"
  ]
}
📄 Logging
Logs are stored in the logs/ directory. Each run or app start creates a new file like:


logs/log_2025-03-26_15-42-17.log
Logged events:

✅ Successful tweet metadata fetch

✅ Replies fetched and filtered

❌ Error responses and exceptions

🔒 Error Handling
Code	Meaning	Reason
400	Bad Request	Invalid or missing tweet ID
401	Unauthorized	Bearer token missing/invalid
500	Internal Server Error	Twitter API error or logic bug
🧪 Test Cases
✅ Tweet with replies → returns matching IDs

✅ Tweet with no replies → returns empty array

✅ Tweet is itself a reply → replies to parent are handled

✅ Invalid tweet ID → proper error response

🤝 Contribution
Feel free to fork the repo, raise issues, and submit PRs.
Contributions and suggestions are always welcome! 🛠️

📜 License
This project is licensed under the MIT License.