from modules.build import GetRepos, Install, Untar, RemoveSource, RemovePreviousVersion
from modules.brand import (
    CreateConfig,
    AddBrandName,
    EditTranslations,
    EditRegistrationURL,
    ChangeLogos,
    EditMobileLinks
)

if __name__ == "__main__":
    # RemoveSource()
    # GetRepos()
    AddBrandName()
    EditTranslations()
    EditRegistrationURL()
    ChangeLogos()
    EditMobileLinks()
    # Install()
    # RemovePreviousVersion()
    # Untar()
    # CreateConfig()
