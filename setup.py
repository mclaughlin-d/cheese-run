from setuptools import setup
from setuptools import find_packages

setup(
    name="cheese-run",
    version="1.0",
    description="A simple game where you play as a mouse collecting cheese.",
    author="Dani McLaughlin, Rebecca Dozortsev",
    author_email="mclaughlin.dani@northeastern.edu",
    url="https://github/mclaughlin-d/cheese-run",
    install_required=["tkinter", "time", "random", "threading", "playsound"],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cheese-run-cli = controller.game_controller:main',
        ],
    },
)