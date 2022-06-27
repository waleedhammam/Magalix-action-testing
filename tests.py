import os
from utils import read_result, send_slack_message


BRANCH = os.environ.get("ENVIRONMENT_BRANCH")

if BRANCH == "main":
    SLACK_CHANNEL = os.environ.get("SLACK_PRD_CHANNEL")
else:
    SLACK_CHANNEL = os.environ.get("SLACK_DEV_CHANNEL")


def run_tests(result: dict):
    summary = {
        "scanned": 5,
        "has_violations": 5,
        "fixed_resources": 4
    }

    assert summary.get("scanned") == result.get("scanned"), "number of scanned resources is wrong"
    assert summary.get("has_violations") == result.get("has_violations"), "number of resources which has violations is wrong"
    assert summary.get("fixed_resources") == result.get("fixed_resources"), "number of fixed resources is wrong"
    assert result.get("pull_request_url"), "auto remediation pr link is wrong"
    assert result.get("auto_remediation_branch"), "auto remediation branch is wrong"


if __name__ == "__main__":
    is_passed = True
    try:
        result = read_result()
        run_tests(result)
    except:
        is_passed = False
        raise
    finally:
        print(BRANCH, SLACK_CHANNEL, is_passed)
