import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from deep_translator import GoogleTranslator

url = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY').json()
img = url['hdurl']
explain = url['explanation']
explainfr = GoogleTranslator(source='auto',target='fr').translate (text=explain)
embed = DiscordEmbed(title="NASA APOD", description=explain)
embedfr = DiscordEmbed(title="NASA Image du jour", description=explainfr)
embed.set_image(img)
embedfr.set_image(img)
webhook = DiscordWebhook(url="webhookurl")
webhook.add_embed(embed)
webhook.add_embed(embedfr)
response = webhook.execute()
