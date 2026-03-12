"""
Discord Webhook Notifications
"""
import requests
import json

# Discord webhook URL for deployments/updates
WEBHOOK_URL = "https://discord.com/api/webhooks/1480530664125239306/zlYI-PWkcYwdyvOFwXW0jtKFkM1-VflpAA0o0NMFrdOsWNVqgz9euUyWTjAvh9sSG8pN"

def send_notification(title, message, color=0x00ff41, fields=None):
    """Send a notification to Discord"""
    
    embed = {
        "title": title,
        "description": message,
        "color": color,
        "footer": {"text": "Web Scraper API"},
        "timestamp": __import__('datetime').datetime.utcnow().isoformat()
    }
    
    if fields:
        embed["fields"] = fields
    
    payload = {
        "embeds": [embed]
    }
    
    try:
        requests.post(WEBHOOK_URL, json=payload, timeout=5)
    except Exception as e:
        print(f"Discord notification failed: {e}")


def notify_new_api_key(name, plan):
    """Notify when a new API key is created"""
    send_notification(
        title="🔑 New API Key Created",
        message=f"A new API key was just created!",
        color=0x00ff41,
        fields=[
            {"name": "Name", "value": name, "inline": True},
            {"name": "Plan", "value": plan, "inline": True}
        ]
    )


def notify_usage_milestone(requests_count, milestone):
    """Notify on usage milestones (100, 1000, 10000 requests)"""
    send_notification(
        title="📊 Usage Milestone",
        message=f"Web Scraper API hit {milestone} requests!",
        color=0x3498db,
        fields=[
            {"name": "Total Requests", "value": str(requests_count), "inline": True}
        ]
    )


def notify_error(url, error):
    """Notify on scraping errors"""
    send_notification(
        title="⚠️ Scrape Error",
        message=f"Failed to scrape URL",
        color=0xff4444,
        fields=[
            {"name": "URL", "value": url[:100], "inline": False},
            {"name": "Error", "value": str(error)[:200], "inline": False}
        ]
    )


def notify_startup():
    """Notify when API starts up"""
    send_notification(
        title="🚀 Web Scraper API Online",
        message="API is now running and ready to accept requests",
        color=0x00ff41
    )