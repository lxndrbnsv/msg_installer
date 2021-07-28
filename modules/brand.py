import os
import json


CONFIG_SAMPLE_PATH = "../qn-messenger-web/config.sample.json"
CONFIG_PATH = "../qn-messenger-web/config.json"

WELCOME_HTML = "../qn-messenger-web/res/welcome.html"
INDEX_HTML = "../qn-messenger-web/src/vector/index.html"
TRANSLATIONS_PATH = "../qn-messenger-web/src/i18n/strings/"

# HOMESERVER = input("homeserver url: ")
# SERVER_NAME = input("server name: ")
# JITSI_URL = input("jitsi url: ")
# BRAND_NAME = input("brand: ")
# REGISTRATION_URL = input("registration url: ")
# API_URL = input("api url: ")

HOMESERVER = "TEST"
SERVER_NAME = "TEST"
JITSI_URL = "TEST"
BRAND_NAME = "TEST"
REGISTRATION_URL = "TEST"
API_URL = "TEST"

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
        def edit_index():
            print("Changing names in index.html")
            with open(INDEX_HTML, "r") as html_file:
                html_data = html_file.read()

            with open(INDEX_HTML, "w") as html_file:
                html_file.write(html_data.replace("Element", BRAND_NAME))

            print("Done!")

        def edit_welcome():
            print("Changing names in welcome.html")
            with open(WELCOME_HTML, "r") as html_file:
                html_data = html_file.read()

            with open(WELCOME_HTML, "w") as html_file:
                html_file.write(html_data.replace("Element", BRAND_NAME))

            print("Done!")

        edit_index()
        edit_welcome()


class EditTranslations:
    def __init__(self):
        print("Updating translations")
        strings_to_translate = [
            "Welcome to Element",
            "Your Element configuration contains invalid JSON. "
            "Please correct the problem and reload the page.",
            "Your Element is misconfigured"
        ]

        translation_files = os.listdir(TRANSLATIONS_PATH)
        for t in translation_files:
            file_path = TRANSLATIONS_PATH + t
            with open(file_path, "r") as json_file:
                json_data = json.load(json_file)

            for string_to_translate in strings_to_translate:
                try:
                    translated_text = json_data[string_to_translate]
                    json_data[translated_text.replace(
                        "Element", BRAND_NAME
                    )] = translated_text.replace("Element", BRAND_NAME)
                except KeyError:
                    pass
            new_data = json.dumps(json_data, indent=4, ensure_ascii=False)
            with open(file_path, "w") as json_file:
                json_file.write(new_data)

        print("Done!")


class ModifyImages:
    def __init__(self):
        pass
