from modules.build import GetRepos, Install, Untar
from modules.brand import CreateConfig, AddBrandName, EditTranslations


if __name__ == "__main__":
    GetRepos()
    CreateConfig()
    AddBrandName()
    EditTranslations()
    Install()
    Untar