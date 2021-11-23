import sys
import json
from utils import read_result

def compare_results(result: dict, expected: dict):
    assert expected.get("scanned") == result.get("scanned"), "number of scanned resources is wrong"
    assert expected.get("has_violations") == result.get("has_violations"), "number of resources which has violations is wrong"
#     assert expected.get("fixed_resources") == result.get("fixed_resources"), "number of fixed resources is wrong"

if __name__ == "__main__":
    expected = json.loads(sys.argv[1])
    result = read_result()
    compare_results(result, expected)
