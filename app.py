from flask import Flask, render_template, request
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import pandas as pd
import os  # <-- added for port

app = Flask(__name__)

# ✅ Telangana district list
telangana_districts = [
    "Adilabad", "Bhadradri Kothagudem", "Hanamkonda", "Hyderabad", "Jagtial", "Jangaon", "Jayashankar Bhupalpally",
    "Jogulamba Gadwal", "Kamareddy", "Karimnagar", "Khammam", "Komaram Bheem Asifabad", "Mahabubabad", "Mahabubnagar",
    "Mancherial", "Medak", "Medchal–Malkajgiri", "Mulugu", "Nagarkurnool", "Nalgonda", "Narayanpet", "Nirmal",
    "Nizamabad", "Peddapalli", "Rajanna Sircilla", "Ranga Reddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad",
    "Wanaparthy", "Warangal", "Yadadri Bhuvanagiri"
]

# ✅ Step 1: Get BBC location ID from city name
def get_location_id(city):
    city = city.strip().lower()
    location_url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode({
        'api_key': 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
        's': city,
        'stack': 'aws',
        'locale': 'en',
        'filter': 'international',
        'place-types': 'settlement,airport,district',
        'a': 'true',
        'format': 'json'
    })

    try:
        result = requests.get(location_url).json()
        locations = result.get('response', {}).get('results', {}).get('results', [])
        if not locations:
            return None
        print(f"📍 Location ID for '{city}': {locations[0]['id']}")  # Debug
        return locations[0]['id']
    except Exception as e:
        print("Location fetch error:", e)
        return None

# ✅ Step 2: Scrape weather data using BBC Weather and location ID
def scrape_weather(city):
    location_id = get_location_id(city)

    # 🛑 Fallback to Hyderabad if not found
    if not location_id:
        fallback = "Hyderabad"
        location_id = get_location_id(fallback)
        if not location_id:
            return {"error": f"No weather data found for '{city}', and fallback also failed."}
        city = f"{city} (Fallback: {fallback})"

    url = f'https://www.bbc.com/weather/{location_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    daily_high_values = soup.find_all('span', attrs={'class': 'wr-day-temperature__high-value'})
    daily_low_values = soup.find_all('span', attrs={'class': 'wr-day-temperature__low-value'})
    daily_summary_tag = soup.find('div', attrs={'class': 'wr-day-summary'})

    if not (daily_high_values and daily_low_values and daily_summary_tag):
        return {"error": "Weather data not available or BBC page layout has changed."}

    daily_summary = daily_summary_tag.text.strip()
    daily_summary_list = re.findall('[a-zA-Z][^A-Z]*', daily_summary)
    datelist = pd.date_range(pd.Timestamp.today(), periods=len(daily_high_values)).tolist()

    weather_data = []
    for i in range(min(12, len(daily_high_values))):
        weather_data.append({
            'name': str(city).capitalize(),
            'date': datelist[i].strftime('%d-%m-%Y'),
            'high': daily_high_values[i].text.strip(),
            'low': daily_low_values[i].text.strip(),
            'summary': daily_summary_list[i] if i < len(daily_summary_list) else ""
        })

    return weather_data

# ✅ Step 3: Flask route to handle GET and POST
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = scrape_weather(city)
    return render_template('index.html', weather_data=weather_data, districts=telangana_districts)

# ✅ Step 4: Run the app with proper host/port (for Render or Heroku)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

