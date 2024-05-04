import requests

def fetch_iss_location():
    url = 'https://api.wheretheiss.at/v1/satellites/25544'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        latitude = data['latitude']
        longitude = data['longitude']
        return latitude, longitude
    else:
        print("Error fetching ISS location:", response.status_code)
        return None, None

def display_iss_location(latitude, longitude):
    if latitude is not None and longitude is not None:
        print(f"Current ISS Location: Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Failed to fetch ISS location.")

def main():
    latitude, longitude = fetch_iss_location()
    display_iss_location(latitude, longitude)

if __name__ == "__main__":
    main()
