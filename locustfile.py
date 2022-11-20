from locust import HttpUser, task
import random

class Tests(HttpUser):
    test_samples = (1, 5, 10, 11, 13, 9, 120, 237846, 934993499, 239429429949, 1234124141241, 124123123120050532)
    @task
    def test_prime_number(self):
        self.client.get(f"prime/{random.choice(self.test_samples)}")
