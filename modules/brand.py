import json


CONFIG_SAMPLE_PATH = "../qn-messenger-web/config.sample.json"
CONFIG_PATH = "../qn-messenger-web/config.json"

WELCOME_HTML = ""
INDEX_HTML = ""
TRANSLATIONS_PATH = ""


HOMESERVER = input("homeserver url: ")
SERVER_NAME = input("server name: ")
JITSI_URL = input("jitsi url: ")
BRAND_NAME = input("brand: ")
LOGO = ""


class CreateConfig:
    def __init__(self):
        print("Generating config file...")
        with open(CONFIG_SAMPLE_PATH, "r") as json_file:
            config_sample_data = json.load(json_file)

        config_sample_data["default_server_config"]["m.homeserver"][
            "base_url"
        ] = HOMESERVER
        config_sample_data["default_server_config"]["m.homeserver"][
            "server_name"
        ] = SERVER_NAME
        config_sample_data["brand"] = BRAND_NAME
        config_sample_data["default_federate"] = False
        config_sample_data["jitsi"]["preferredDomain"] = JITSI_URL

        config = json.dumps(config_sample_data, indent=2)
        with open(CONFIG_PATH, "w") as json_file:
            json_file.write(config)

        print("Done!")


class AddBrandName:
    def __init__(self):
        pass


class AddTranslation:
    def __init__(self):
        pass


class ModifyImages:
    def __init__(self):
        pass
