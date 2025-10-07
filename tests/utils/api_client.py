import requests

class APIClient:
    BASE_URL = "https://demoqa.com"

    def get_books(self):
        response = requests.get(f"{self.BASE_URL}/BookStore/v1/Books")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("API request failed")
