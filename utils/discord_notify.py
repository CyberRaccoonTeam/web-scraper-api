"""
Discord Webhook Notifications for Web Scraper API
"""
import requests
from datetime import datetime

# Discord webhook URL for deployments
WEBHOOK_URL = "https://discord.com/api/webhooks/1480530664125239306/zlYI-PWkcYwdyvOFwXW0jtKFkM1-VflpAA0o0NMFrdOsWNVqgz9euUyWTjAvh9sSG8pN"


def send_notification(title, message, color=0x00ff41, fields=None):
    """Send a notification to Discord"""
    
    embed = {
        "title": title,
        "description": message,
        "color": color,
        "footer": {"text": "🦝 Web Scraper API"},
        "timestamp": datetime.utcnow().isoformat()
    }
    
    if fields:
        embed["fields"] = fields
    
    payload = {"embeds": [embed]}
    
    try:
        requests.post(WEBHOOK_URL, json=payload, timeout=5)
        return True
    except Exception as e:
        print(f"Discord notification failed: {e}")
        return False


def notify_new_api_key(name, plan, requests_limit):
    """Notify when a new API key is created"""
    return send_notification(
        title="🔑 New API Key Created",
        message=f"A new API key was registered",
        color=0x00ff41,
        fields=[
            {"name": "Name", "value": name, "inline": True},
            {"name": "Plan", "value": plan.upper(), "inline": True},
            {"name": "Requests Limit", "value": f"{requests_limit}/mo", "inline": True}
        ]
    )


def notify_usage_milestone(total_requests, milestone):
    """Notify on usage milestones"""
    return send_notification(
        title="📊 Usage Milestone",
        message=f"Web Scraper API hit **{milestone}** total requests!",
        color=0x3498db,
        fields=[
            {"name": "Total Requests", "value": str(total_requests), "inline": True}
        ]
    )


def notify_error(url, error_message):
    """Notify on scraping errors (high priority only)"""
    return send_notification(
        title="⚠️ Scrape Error",
        message=f"Failed to extract data from URL",
        color=0xff4444,
        fields=[
            {"name": "URL", "value": url[:100] if len(url) > 100 else url, "inline": False},
            {"name": "Error", "value": error_message[:200] if len(error_message) > 200 else error_message, "inline": False}
        ]
    )


def notify_startup(port):
    """Notify when API starts up"""
    return send_notification(
        title="🚀 Web Scraper API Online",
        message=f"API is now running on port {port}",
        color=0x00ff41,
        fields=[
            {"name": "Health Check", "value": f"http://localhost:{port}/health", "inline": False}
        ]
    )