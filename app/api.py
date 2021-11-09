import json
import requests

class API:
    def __init__(self, url: str) -> None:
        self._url = url

    def get_member(self, member_id: int) -> dict:
        r = requests.get(self._url, params={'member_id': member_id})
        
        if r.status_code == 200:
            return json.loads(r.text)
        
        return {}