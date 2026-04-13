# Web Scraper API

![RaccoonLabs](https://img.shields.io/badge/Built%20by-RaccoonLabs-blueviolet)

REST API for web scraping — send a URL, get clean structured data back.

## What It Does
Part of the **RaccoonLabs API Suite**. This Flask-based REST API accepts URLs and returns extracted, cleaned content — text, links, images, and metadata. Supports JavaScript-rendered pages via headless browser integration. Stripe-powered pricing with 3 tiers: **Starter $9/mo**, **Pro $29/mo**, **Enterprise $99/mo**.

## Tech Stack
- Python 3.10+, Flask
- BeautifulSoup, Playwright
- Stripe API

## Quick Start
```bash
git clone https://github.com/CyberRaccoonTeam/web-scraper-api.git
cd web-scraper-api
pip install -r requirements.txt
flask run
# POST /scrape {"url": "https://example.com"}
```

## Pricing
| Tier | Price | Requests/mo |
|------|-------|-------------|
| Starter | $9 | 5,000 |
| Pro | $29 | 25,000 |
| Enterprise | $99 | Unlimited |

## License
MIT License

## Links
- **RaccoonLabs:** https://github.com/CyberRaccoonTeam
