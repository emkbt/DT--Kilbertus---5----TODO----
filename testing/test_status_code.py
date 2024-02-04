import unittest
import requests

class TestTodoListAPI(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"
    api_key = "83a426cd48bdbae86c217bf2217bd038"
    accepted_codes = [200]
    
    def test_add_task(self):
        url = f"{self.base_url}/add?api_key={self.api_key}"
        payload = {"description": "Study"}
        response = requests.put(url, headers=payload)
        
        self.assertEqual(response.status_code in self.accepted_codes, True)

    def test_auth(self):
        url = f"{self.base_url}/auth?api_key={self.api_key}"
        response = requests.get(url)

        self.assertEqual(response.status_code in self.accepted_codes, True)

    def test_get_tasks(self):
        url = f"{self.base_url}/tasks?api_key={self.api_key}"
        response = requests.get(url)

        self.assertEqual(response.status_code in self.accepted_codes, True)

    def test_delete_task(self):
        url = f"{self.base_url}/delete?api_key={self.api_key}"
        payload = {"description": "Study"}
        response = requests.delete(url, headers=payload)

        self.assertEqual(response.status_code in self.accepted_codes, True)

    def test_complete_task(self):
        url = f"{self.base_url}/complete?api_key={self.api_key}"
        payload = {"description": "Study"}
        response = requests.post(url, headers=payload)

        self.assertEqual(response.status_code in self.accepted_codes, True)

if __name__ == "__main__":
    unittest.main()