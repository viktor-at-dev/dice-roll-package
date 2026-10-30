from setuptools import setup, find_packages

setup(
    name="your_package_name",  # e.g., "dice_roller_v"
    version="0.1.0",
    author="Victor",
    description="A simple dice rolling utility package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)