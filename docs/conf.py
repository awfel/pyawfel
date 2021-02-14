import sphinx_rtd_theme  # noqa: F401

extensions = [
    "sphinx_rtd_theme",
]

html_theme = "sphinx_rtd_theme"
html_logo = "./awfel_small.png"
html_title = "pyawfel"

copyright = "2020-2021, James Warne"
project = "pyawfel"
author = "James Warne"

html_theme_options = {
    "navigation_depth": 4,
}

html_context = {
    "display_github": True,
    "github_username": "awfel",
    "github_repo": "pyawfel",
    "github_version": "main/docs/"
}
