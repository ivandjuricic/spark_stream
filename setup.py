from setuptools import (
    find_packages,
    setup
)

setup(
    name="spark_streaming",
    version="0.0.5",
    description="Testing for pyspark stream distribution",
    long_description="Databricks offers a way to install libraries from pypi so testing this feature",
    url=("http://https://pypi.playstudios-il.com/service/rest/repository/browse/"
         "playstudios-pypi/psil_mode_client/"),
    author="MagicOPS",
    author_email="ivand@playstudios-il.com",
    license="MY LICNCE",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: PlayStudios :: PlayStudios-IL",
        "Programming Language :: Python :: 3.7"
    ],
    keywords="databricks",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[],
    include_package_data=True
)
