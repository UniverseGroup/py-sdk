import setuptools

version = "0.0.1"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="universelist",
    version=version,
    author="Universelist",
    author_email="insanephin@gmail.com",
    description="A Official SDK for the Universelist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    project_urls={
        "Homepage": "https://universelist.kr",
        "Source": "https://github.com/UniverseGroup/py-sdk",
        "Documentation": "https://universelist.github.io/py-sdk/",
    },
    url="https://github.com/UniverseGroup/py-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/UniverseGroup/py-sdk/issues",
    },
    packages=["universelist"],
    package_data={"universelist": ["py.typed"]},
    include_package_data=True,
    python_requires=">= 3.6",
    install_requires=requirements,
    keywords="discord bot list discordbots botlist universelist universe",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)