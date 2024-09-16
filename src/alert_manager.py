import smtplib
from email.mime.text import MIMEText
import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def send_alert(subject, message):
    config = load_config()
    email_config = config["alerting"]["email"]
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = email_config["username"]
    msg["To"] = email_config["to"]

    with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
        server.starttls()
        server.login(email_config["username"], email_config["password"])
        server.send_message(msg)

if __name__ == "__main__":
    send_alert("Test Alert", "This is a test alert message.")

# You have to use SECRETS everywhere, don't forget about it mate =D
