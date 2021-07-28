import os
import json
import subprocess


CONFIG_SAMPLE_PATH = "/var/www/test.msg.mybusines.app/msg/config.sample.json"
CONFIG_PATH = "/var/www/test.msg.mybusines.app/msg/config.json"

WELCOME_HTML = "./qn-messenger-web/res/welcome.html"
INDEX_HTML = "./qn-messenger-web/src/vector/index.html"
TRANSLATIONS_PATH = "./qn-messenger-web/src/i18n/strings/"

REACT_SDK_LOGIN_PAGE = "./qn-matrix-react-sdk/src/components/structures/MatrixChat.tsx"
REACT_SDK_HOMEPAGE = "./qn-matrix-react-sdk/src/components/structures/HomePage.tsx"

HOMESERVER = input("homeserver url: ")
SERVER_NAME = input("server name: ")
JITSI_URL = input("jitsi url: ")
BRAND_NAME = input("brand: ")
REGISTRATION_URL = input("registration url: ")
API_URL = input("api url: ")

IMAGES_DIR = "./images/" + input("images directory (no slash in the end): ")


class CreateConfig:
    def __init__(self):
        print("Generating config file..")
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
                    json_data[string_to_translate.replace(
                        "Element", BRAND_NAME
                    )] = translated_text.replace("Element", BRAND_NAME)
                except KeyError:
                    pass
            new_data = json.dumps(json_data, indent=4, ensure_ascii=False)
            with open(file_path, "w") as json_file:
                json_file.write(new_data)

        print("Done!")


class EditRegistrationURL:
    def __init__(self):
        print("Editing registration links")

        def modify_welcome():
            with open(WELCOME_HTML, "r") as html_file:
                html_data = html_file.read()

            with open(WELCOME_HTML, "w") as html_file:
                html_file.write(
                    html_data.replace(
                        "#/register", REGISTRATION_URL
                    )
                )

        def modify_login_page():
            with open(REACT_SDK_LOGIN_PAGE, "r") as tsx_file:
                tsx_data = tsx_file.read()

            with open(REACT_SDK_LOGIN_PAGE, "w") as tsx_file:
                tsx_file.write(
                    tsx_data.replace(
                        'this.showScreen("forgot_password");',
                        f'window.open("{REGISTRATION_URL}");'
                    ).replace(
                        'this.showScreen("register");',
                        'window.open("https://qaim.me/auth");'
                    )
                )
        modify_welcome()
        modify_login_page()

        print("Done!")


class ChangeLogos:
    def __init__(self):
        favicon = f"{IMAGES_DIR}/favicon.ico"
        logo = f"{IMAGES_DIR}/logo.svg"

        def replace_favicon():
            replace_command = "rm ./qn-messenger-web/res/vector-icons/favicon.ico && " \
                              f"cp {favicon} ./qn-messenger-web/res/vector-icons/"
            fav_replace = subprocess.Popen(
                replace_command, stdout=subprocess.PIPE, shell=True
            )
            out = fav_replace.stdout.read().decode()
            print(out)

        def replace_logos():
            replace_command = "rm ./qn-messenger-web/res/themes/element/img/" \
                              "logos/element-logo.svg && " \
                              "rm ./qn-messenger-web/res/welcome/images/logo.svg && " \
                              f"cp {logo} ./qn-messenger-web/res/themes/element/img/" \
                              f"logos/element-logo.svg && " \
                              f"cp {logo} ./qn-messenger-web/res/welcome/" \
                              f"images/logo.svg"
            logo_replace = subprocess.Popen(
                replace_command, stdout=subprocess.PIPE, shell=True
            )
            out = logo_replace.stdout.read().decode()
            print(out)

        replace_favicon()
        replace_logos()
