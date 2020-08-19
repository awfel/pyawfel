from setuptools import setup, find_packages

with open('./README.md', 'rt', encoding='utf8') as f:
    long_description = f.read()

setup(
    name="awfel",
    version="0.0.1.pre",
    packages=find_packages(),
    authors="James Warne",
    author_email="bebleo@yahoo.com",
    long_description=long_description,
    python_requires=">=3.6",
    install_requires=[
        "semver",
        "jinja2"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "smtpdfix >= 0.2.4"
        ],
        "lint": ["flake8"],
        "docs": ["sphinx", "sphinx_rtd_theme"]
    }
)
