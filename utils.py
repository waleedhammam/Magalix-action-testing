import json
import requests


def read_result():
    with open("result.json") as f:
        return json.load(f)


def send_slack_message(branch: str, slack_channel: str, is_passed: bool):
    payload = {
        "type": "mrkdwn",
        "attachments": [
            {
                "title": "Github Action E2E Test",
                "fields": [{"title": "Branch", "value": branch}],
                "color": "good" if is_passed else "danger",
            }
        ],
    }
    response = requests.post(slack_channel, json=payload)
    response.raise_for_status()
