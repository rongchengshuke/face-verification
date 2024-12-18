import json
import time

import colored_traceback
import requests

from a002_model.a001_utils.a000_CONFIG import FASTAPI_PORT
from a002_model.a001_utils.a002_general_utils import get_time_stamp_str

colored_traceback.add_hook()

# API_URL = rf"http://127.0.0.1:{FASTAPI_PORT}"
API_URL = rf"http://172.29.248.181:{FASTAPI_PORT}"

BASE64_TXT_PATH_0 = r"a003_fastapi/a002_base64_post_test/base64/p1_0.txt"
BASE64_TXT_PATH_1 = r"a003_fastapi/a002_base64_post_test/base64/p2_0.txt"


def read_base64_from_file(file_path: str) -> str:
    """从文件读取base64字符串"""
    with open(file_path, 'r') as f:
        return f.read().strip()


def post_image_pair_base64(
        base64_path_0: str,
        base64_path_1: str,
        api_url: str
) -> dict:
    """
    从指定路径读取base64字符串并发送请求
    """
    base64_image_0 = read_base64_from_file(base64_path_0)
    base64_image_1 = read_base64_from_file(base64_path_1)

    endpoint = f"{api_url}/facecomparsion"

    json_data = {
        "image_0": base64_image_0,
        "image_1": base64_image_1
    }

    response = requests.post(
        url=endpoint,
        json=json_data,
        headers={"accept": "application/json"}
    )

    response.raise_for_status()
    return response.json()


def test_post_image_pair_base64():
    result = post_image_pair_base64(
        base64_path_0=BASE64_TXT_PATH_0,
        base64_path_1=BASE64_TXT_PATH_1,
        api_url=API_URL
    )
    result_str = json.dumps(result, indent=4, ensure_ascii=False)
    print(result_str)


if __name__ == "__main__":
    start_timestamp = get_time_stamp_str()

    for i in range(10):
        test_post_image_pair_base64()

    end_timestamp = get_time_stamp_str()

    print(
        f"Start at {start_timestamp}, end at {end_timestamp}"
    )
