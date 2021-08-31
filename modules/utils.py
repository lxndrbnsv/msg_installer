import json


class ReadConfig:
    def __init__(self):
        with open("./config.json", "r") as json_file:
            config_data = json.load(json_file)

        self.config_sample_path = config_data["config_sample_path"]
        self.config_path = config_data["config_path"]
        self.welcome_html = config_data["welcome_html"]
        self.index_html = config_data["index_html"]
        self.translations_path = config_data["translations_path"]
        self.react_sdk_login_page = config_data["react_sdk_login_page"]
        self.react_sdk_homepage = config_data["react_sdk_homepage"]
        self.homeserver = config_data["homeserver"]
        self.server_name = config_data["server_name"]
        self.jitsi_url = config_data["jitsi_url"]
        self.brand_name = config_data["brand_name"]
        self.registration_url = config_data["registration_url"]
        self.forgot_password_url = config_data["forgot_password_url"]
        self.api_url = config_data["api_url"]
        self.messenger_url = config_data["messenger_url"]
        self.images_dir = config_data["images_dir"]
        self.messenger_path = config_data["messenger_path"]