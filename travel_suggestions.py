
class TravelSuggestions:
   GOOGLE_PLACES_API_KEY = "YOUR_GOOGLE_PLACES_API_KEY"
   @staticmethod
   def find_eco_activities(location):
       """Find eco-friendly activities near a location."""
       url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
       params = {
           "location": location,
           "radius": 5000,
           "keyword": "eco-friendly",
           "key": TravelSuggestions.GOOGLE_PLACES_API_KEY,
       }
       response = requests.get(url, params=params)
       return response.json().get("results", [])
   @staticmethod
   def find_eco_hotels(location):
       """Find eco-friendly hotels near a location."""
       url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
       params = {
           "location": location,
           "radius": 5000,
           "keyword": "eco-friendly hotel",
           "key": TravelSuggestions.GOOGLE_PLACES_API_KEY,
       }
       response = requests.get(url, params=params)
       return response.json().get("results", [])