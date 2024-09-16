import requests
import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def fetch_osint_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def collect_data(sources):
    data = []
    for source in sources:
        data.extend(fetch_osint_data(source))
    return data

if __name__ == "__main__":
    config = load_config()
    osint_sources = config["osint_sources"]
    data = collect_data(osint_sources)
    print(data)
