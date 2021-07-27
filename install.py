from modules.build import GetRepos, Install
from modules.brand import CreateConfig


if __name__ == "__main__":
    GetRepos()
    Install()
    CreateConfig()
