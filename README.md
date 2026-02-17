
# Simple Chat Agent (v4)

This is a simple chat agent built with Flask and can be hosted on Render.

## How to Deploy on Render

1.  **Fork or Use this Repository:** Ensure this code is in your GitHub account.
2.  **Create a New Web Service on Render:**
    *   Go to [Render Dashboard](https://dashboard.render.com/).
    *   Click **New +** and select **Web Service**.
    *   Connect your GitHub account and select this repository (`simple-chat-agent-v4`).
3.  **Configure the Service:**
    *   **Name:** `simple-chat-agent-v4`
    *   **Environment:** `Python 3`
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `gunicorn app:app`
4.  **Deploy:** Click **Create Web Service**.

Once deployed, you can open the URL provided by Render to talk to your agent!
