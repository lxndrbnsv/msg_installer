from modules.build import GetRepos, Install, Untar
from modules.brand import CreateConfig, AddBrandName, EditTranslations


if __name__ == "__main__":
    GetRepos()
    AddBrandName()
    EditTranslations()
    Install()
    Untar()
    CreateConfig()
