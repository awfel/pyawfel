from setuptools import find_packages, setup

with open('./README.md', 'rt', encoding='utf8') as f:
    long_description = f.read()

setup(
    name="awfel",
    version="0.0.1.pre",
    packages=find_packages(),
    authors="James Warne",
    author_email="bebleo@yahoo.com",
    long_description=long_description,
    python_requires=">= 3.6",
    install_requires=[
        "semver",
        "jinja2"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "smtpdfix >= 0.2.5"
        ],
        "lint": ["flake8", "isort"],
        "docs": ["sphinx", "sphinx_rtd_theme"]
    }
)
