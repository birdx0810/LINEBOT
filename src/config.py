# -*- coding: UTF-8 -*-
# Import system modules
import os
import json

def get_server_config():
    """
    Get server configurations
    """
    path = os.path.abspath(
        f"{os.path.abspath(__file__)}/../../config.json"
    )

    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist")

    with open(path, "r") as config_file:
        config = json.load(config_file)

    return config
