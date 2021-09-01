import os
import json
import subprocess

from modules.utils import ReadConfig


class CreateConfig:
    def __init__(self):
        cfg = ReadConfig()
        print("Generating config file..")
        with open(cfg.config_sample_path, "r") as json_file:
            config_sample_data = json.load(json_file)

        config_sample_data["default_server_config"]["m.homeserver"][
            "base_url"
        ] = cfg.homeserver
        config_sample_data["default_server_config"]["m.homeserver"][
            "server_name"
        ] = cfg.server_name
        config_sample_data["brand"] = cfg.brand_name
        config_sample_data["default_federate"] = False
        config_sample_data["jitsi"]["preferredDomain"] = cfg.jitsi_url

        config = json.dumps(config_sample_data, indent=2)
        with open(cfg.config_path, "w") as json_file:
            json_file.write(config)

        print("Done!")


class AddBrandName:
    def __init__(self):
        cfg = ReadConfig()

        def edit_index():
            print("Changing names in index.html")
            with open(cfg.index_html, "r") as html_file:
                html_data = html_file.read()

            with open(cfg.index_html, "w") as html_file:
                html_file.write(html_data.replace("Element", cfg.brand_name))

            print("Done!")

        def edit_welcome():
            print("Changing names in welcome.html")
            with open(cfg.welcome_html, "r") as html_file:
                html_data = html_file.read()

            with open(cfg.welcome_html, "w") as html_file:
                html_file.write(html_data.replace("Element", cfg.brand_name))

            print("Done!")

        def edit_mobile_guide():
            print("Changing names in mobile_guide...")
            with open(cfg.mobile_guide_path, "r") as html_file:
                html_data = html_file.read()

            with open(cfg.mobile_guide_path, "w") as html_file:
                html_file.write(
                    html_data.replace(
                        "Set up Element on iOS or Android",
                        f"Set up {cfg.brand_name} on iOS or Android"
                    )
                )

            print("Done!")

        edit_index()
        edit_welcome()
        edit_mobile_guide()


class EditTranslations:
    def __init__(self):
        cfg = ReadConfig()

        print("Updating translations")
        strings_to_translate = [
            "Welcome to Element",
            "Your Element configuration contains invalid JSON. "
            "Please correct the problem and reload the page.",
            "Your Element is misconfigured"
        ]

        translation_files = os.listdir(cfg.translations_path)
        for t in translation_files:
            file_path = cfg.translations_path + t
            with open(file_path, "r") as json_file:
                json_data = json.load(json_file)

            for string_to_translate in strings_to_translate:
                try:
                    translated_text = json_data[string_to_translate]
                    json_data[string_to_translate.replace(
                        "Element", cfg.brand_name
                    )] = translated_text.replace("Element", cfg.brand_name)
                except KeyError:
                    pass
            new_data = json.dumps(json_data, indent=4, ensure_ascii=False)
            with open(file_path, "w") as json_file:
                json_file.write(new_data)

        print("Done!")


class EditRegistrationURL:
    def __init__(self):
        cfg = ReadConfig()

        print("Editing registration links")

        def modify_welcome():
            with open(cfg.welcome_html, "r") as html_file:
                html_data = html_file.read()

            with open(cfg.welcome_html, "w") as html_file:
                html_file.write(
                    html_data.replace(
                        "#/register", f"{cfg.registration_url}?returl={cfg.messenger_url}"
                    )
                )

        def modify_login_page():
            with open(cfg.react_sdk_login_page, "r") as tsx_file:
                tsx_data = tsx_file.read()

            with open(cfg.react_sdk_login_page, "w") as tsx_file:
                tsx_file.write(
                    tsx_data.replace(
                        'this.showScreen("forgot_password");',
                        f'location.href="{cfg.forgot_password_url}&returl=" + location.href;'
                    ).replace(
                        'this.showScreen("register");',
                        f'location.href = "{cfg.registration_url}?returl=" + location.href;'
                    )
                )
        modify_welcome()
        modify_login_page()

        print("Done!")


class ChangeLogos:
    def __init__(self):
        cfg = ReadConfig()

        favicon = f"{cfg.images_dir}/favicon.ico"
        logo = f"{cfg.images_dir}/logo.svg"

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


class EditMobileLinks:
    def __init__(self):
        cfg = ReadConfig()
        print("Changing links in mobile guide...")
        with open(cfg.mobile_guide_path, "r") as html_file:
            html_data = html_file.read()
        with open(cfg.mobile_guide_path, "w") as html_file:
            html_file.write(
                html_data.replace(
                    "https://apps.apple.com/app/vector/id1083446067",
                    cfg.ios_app_url
                ).replace(
                    "https://play.google.com/store/apps/details?id=im.vector.app",
                    cfg.android_app_url
                )
            )

        print("Done!")
