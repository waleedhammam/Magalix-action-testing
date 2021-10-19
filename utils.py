import json
import requests


def read_result():
    with open("result.json") as f:
        return json.load(f)


def send_slack_message(branch: str, slack_channel: str, is_passed: bool):
    status = "SUCCESS" if is_passed else "FAILURE"
    env = "PROD" if branch == "main" else "DEV"

    message = f"{status}: E2E Compliance Enforcement Test on\n{env}: `{branch}`"
    payload = {
        "type": "mrkdwn",
        "attachments": [
            {
                "fields": [{"value": message, "short": "false"}],
                "color": "good" if is_passed else "danger",
                 "ts":  "timestamp"
            }
        ],
    }
    response = requests.post(slack_channel, json=payload)
    response.raise_for_status()
