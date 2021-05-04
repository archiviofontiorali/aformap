import time

import geopy


class GEOLocator:
    def __init__(self):
        self._language = "it"
        self._user_agent = "aformap/v0.1.0"
        self._locator = geopy.geocoders.Nominatim(user_agent=self._user_agent)

    def geocode(self, address) -> (float, float):
        location = self._locator.geocode(address, language=self._language)
        latitude = getattr(location, "latitude", None)
        longitude = getattr(location, "longitude", None)
        time.sleep(1)  # Ensure 1 second is passed
        return latitude, longitude
