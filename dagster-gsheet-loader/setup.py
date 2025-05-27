from setuptools import find_packages, setup

setup(
    name="dagster_gsheet_loader",
    packages=find_packages(exclude=["dagster_gsheet_loader_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
