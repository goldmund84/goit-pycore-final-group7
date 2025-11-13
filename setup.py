"""
Setup configuration for Personal Assistant package.
"""

from setuptools import setup, find_packages

setup(
    name="personal-assistant",
    version="1.0.0",
    author="goit-pycore-final-group7",
    description="Personal Assistant CLI for managing contacts and notes",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "personal-assistant=personal_assistant.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
