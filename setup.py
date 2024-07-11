# setup.py

import setuptools

setuptools.setup(
    name="OctoPrint-FilamentManager",
    version="0.1.1",
    author="toooomm",
    author_email="peterotzi79@gmail.com",
    description="Manage filaments used in your prints with OctoPrint",
    entry_points={
        "octoprint.plugin": [
            "filamentmanager = octoprint_filamentmanager"
        ]
    },
    install_requires=[
        "octoprint"
    ],
    packages=setuptools.find_packages()
)
