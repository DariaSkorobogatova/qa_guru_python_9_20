import json
import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def post_query(url, **kwargs):
    with step(f"POST {url}"):
        response = requests.post(url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(
            body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt"
        )
        logging.info(curlify.to_curl(response.request))
        return response

