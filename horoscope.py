import requests

def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    Accepted values: Aries, Taurus, Gemini, 
    Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, 
    Capricorn, Aquarius, Pisces
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return: dict - JSON DATA
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)
    print("URL:", response.url)
    print("Response Text:", response.text)

    return response.json()

