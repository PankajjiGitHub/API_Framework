import requests
import yaml

#this function loads the configuration from a YAML file
def load_config():
    return yaml.safe_load(open("conf/config.yaml"))

#This class will handle all API requests
class RequestHandler:
    def __init__(self):
        cfg = load_config()
        self.base = cfg["base_url"].rstrip('/')
        self.session = requests.Session()

    def send(self, method, end_point, **kwargs):
        url = f"{self.base}{end_point}"
        resp = self.session.request(method, url, **kwargs)
        return resp.json()
    
