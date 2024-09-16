import requests
import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def update_rules(rules):
    config = load_config()
    firewall_config = config["firewall"]
    response = requests.post(
        f"http://{firewall_config['host']}:{firewall_config['port']}/update-rules",
        headers={"Authorization": f"Bearer {firewall_config['api_key']}"},
        json={"rules": rules}
    )
    response.raise_for_status()

if __name__ == "__main__":
    rules = [...] 
    update_rules(rules)
