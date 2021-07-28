from modules.build import GetRepos, Install, Untar
from modules.brand import (
    CreateConfig,
    AddBrandName,
    EditTranslations,
    EditRegistrationURL,
    ChangeLogos
)


if __name__ == "__main__":
    GetRepos()
    AddBrandName()
    EditTranslations()
    EditRegistrationURL()
    ChangeLogos()
    Install()
    Untar()
    CreateConfig()
