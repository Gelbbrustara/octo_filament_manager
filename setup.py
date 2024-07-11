from setuptools import setup

setup(
    name="octoprint_filament_manager",
    version="0.1.0",
    description="OctoPrint Plugin for print management and filament monitoring",
    author="Gelbbrustara",
    packages=["octoprint_filament_manager"],
    include_package_data=True,
    install_requires=[
        "OctoPrint>=1.4.0",
        "SQLAlchemy"
    ],
    entry_points={
        "octoprint.plugin": [
            "filament_manager = octoprint_filament_manager"
        ]
    }
)
