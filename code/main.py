import requests
import time
from datetime import datetime
from pprint import pprint

# CONFIGURATION
DISTRICT_ID = ***  # Replace with your district ID
CHECK_INTERVAL = 60  # in seconds
AGE_LIMIT = 18  # Minimum age (18 or 45)
MIN_DOSES = 1  # Minimum available capacity to alert
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_today_date():
    return datetime.today().strftime("%d-%m-%Y")

def fetch_slots(district_id, date):
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    params = {
        "district_id": district_id,
        "date": date
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def filter_available_centers(data, age_limit=18, min_capacity=1):
    available_centers = []
    if not data:
        return available_centers

    for center in data.get("centers", []):
        for session in center.get("sessions", []):
            if (
                session["min_age_limit"] <= age_limit
                and session["available_capacity"] >= min_capacity
            ):
                available_centers.append({
                    "name": center["name"],
                    "date": session["date"],
                    "vaccine": session["vaccine"],
                    "available": session["available_capacity"],
                    "pincode": center["pincode"]
                })
    return available_centers

def display_slots(slots):
    if slots:
        print(f"\n🚨 Slots available! ({len(slots)} centers)")
        for slot in slots:
            print(f"- {slot['name']} ({slot['pincode']}) | {slot['date']} | "
                  f"{slot['vaccine']} | Doses: {slot['available']}")
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] No slots available.")

def main():
    print("💉 CoWIN Vaccine Slot Checker started...")
    while True:
        today = get_today_date()
        data = fetch_slots(DISTRICT_ID, today)
        slots = filter_available_centers(data, AGE_LIMIT, MIN_DOSES)
        display_slots(slots)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
