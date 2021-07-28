from modules.build import GetRepos, Install, Untar, RemoveSource, RemovePreviousVersion
from modules.brand import (
    CreateConfig,
    AddBrandName,
    EditTranslations,
    EditRegistrationURL,
    ChangeLogos
)


if __name__ == "__main__":
    RemoveSource()
    GetRepos()
    AddBrandName()
    EditTranslations()
    EditRegistrationURL()
    ChangeLogos()
    Install()
    RemovePreviousVersion()
    Untar()
    CreateConfig()
