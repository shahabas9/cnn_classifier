import setuptools
__version__= "0.0.1"
repo_name="CNN_CLASSIFIER"
author_name="shahabas9"
src_repo="cnn_classifier"
author_email="mohdshahabasm@gmail.com"

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

setuptools.setup(
    name=src_repo,
    version= __version__,
    author=author_name,
    author_email=author_email,
    description="this is my claasification project using cnn",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{author_name}/{src_repo}",
    project_urls={
        "Bug Tracker" :f"https://github.com/{author_name}/{src_repo}"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
