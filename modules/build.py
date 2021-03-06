import os
import subprocess

from modules.utils import ReadConfig


class GetRepos:
    def __init__(self):
        repo_list = [
            "https://github.com/lxndrbnsv/qn-matrix-js-sdk.git",
            "https://github.com/lxndrbnsv/qn-matrix-react-sdk.git",
            "https://github.com/lxndrbnsv/qn-messenger-web.git",
        ]
        for repo in repo_list:
            clone_repo = f"git clone --branch master {repo}"
            command = subprocess.Popen(clone_repo, stdout=subprocess.PIPE, shell=True)
            out = command.stdout.read().decode()
            print(out)


class Install:
    def __init__(self):
        def install_js_sdk():
            print("Installing js-sdk...")
            install_sdk = "pushd qn-matrix-js-sdk && yarn link && yarn install && popd"
            install_component = subprocess.Popen(
                install_sdk, stdout=subprocess.PIPE, shell=True, executable="/bin/bash"
            )
            out = install_component.stdout.read().decode()
            print(out)

        def install_react_sdk():
            print("Installing react-sdk...")
            install_sdk = (
                "pushd qn-matrix-react-sdk && yarn link && "
                "yarn link matrix-js-sdk && yarn install && yarn reskindex && popd"
            )
            install_component = subprocess.Popen(
                install_sdk, stdout=subprocess.PIPE, shell=True, executable="/bin/bash"
            )
            out = install_component.stdout.read().decode()
            print(out)

        def build_messenger():
            print("Installing web client...")
            build_msg = (
                "cd qn-messenger-web && yarn link matrix-js-sdk &&"
                " yarn link matrix-react-sdk && yarn install &&"
                " yarn reskindex && yarn dist"
            )
            # build_msg = "cd element-web && yarn dist"
            install_component = subprocess.Popen(
                build_msg, stdout=subprocess.PIPE, shell=True, executable="/bin/bash"
            )
            out = install_component.stdout.read().decode()
            print(out)

        install_js_sdk()
        install_react_sdk()
        build_messenger()


class Untar:
    def __init__(self):
        messenger_path = ReadConfig().messenger_path
        dist_name = os.listdir("./qn-messenger-web/dist")[0]
        untar_command = f"cp ./qn-messenger-web/dist/{dist_name} " \
                        f"{messenger_path} && cd {messenger_path} && " \
                        f"tar -zxvf {dist_name} && ln" \
                        f" -s {dist_name.replace('.tar.gz', '')} msg"
        untar = subprocess.Popen(untar_command, stdout=subprocess.PIPE, shell=True)
        out = untar.stdout.read().decode()
        print(out)


class RemoveSource:
    def __init__(self):
        remove_command = "rm -rf qn-m*"
        remove = subprocess.Popen(
            remove_command, stdout=subprocess.PIPE, shell=True
        )
        out = remove.stdout.read().decode()
        print(out)


class RemovePreviousVersion:
    def __init__(self):

        remove_command = f"rm -rf {ReadConfig().messenger_path}*"
        remove = subprocess.Popen(
            remove_command, stdout=subprocess.PIPE, shell=True
        )
        out = remove.stdout.read().decode()
        print(out)
