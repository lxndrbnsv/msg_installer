import subprocess



def download_repos():
    repo_list = [
        "https://github.com/lxndrbnsv/matrix-js-sdk.git",
        "https://github.com/lxndrbnsv/matrix-react-sdk.git",
        "https://github.com/lxndrbnsv/element-web.git"
    ]
    for repo in repo_list:
        clone_repo = f"git clone --branch master {repo}"
        command = subprocess.Popen(clone_repo, stdout=subprocess.PIPE, shell=True)
        out = command.stdout.read().decode()
        print(out)


def install_js_sdk():
    print("Installing js-sdk...")
    install_sdk = "pushd matrix-js-sdk && yarn link && yarn install && popd"
    install_component = subprocess.Popen(install_sdk, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
    out = install_component.stdout.read().decode()
    print(out)


def install_react_sdk():
    print("Installing react-sdk...")
    install_sdk = "pushd matrix-react-sdk && yarn link && yarn link matrix-js-sdk && yarn install && popd"
    install_component = subprocess.Popen(install_sdk, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
    out = install_component.stdout.read().decode()
    print(out)


def build_messenger():
    print("Installing web client...")
    build_msg = "cd element-web && yarn link matrix-js-sdk && yarn link matrix-react-sdk && yarn install && yarn reskindex && yarn dist"
    # build_msg = "cd element-web && yarn dist"
    install_component = subprocess.Popen(build_msg, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
    out = install_component.stdout.read().decode()
    print(out)


if __name__ == "__main__":
    # download_repos()
    install_js_sdk()
    install_react_sdk()
    build_messenger()
