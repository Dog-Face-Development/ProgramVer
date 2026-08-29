"""Setup file for ProgramVer."""

from setuptools import setup, find_packages


def readme():
    """Reads the README.md file."""
    with open("README.md", encoding="UTF-8") as f:
        return f.read()


setup(
    name="programver",
    version="2.0.0",
    description="A customizable version dialog for Python applications, "
    "inspired by Microsoft's winver.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: User Interfaces",
    ],
    keywords="program version windows winver microsoft license gui",
    url="https://github.com/willtheorangeguy/ProgramVer",
    author="willtheorangeguy",
    packages=find_packages(include=["programver", "programver.*"]),
    package_data={"programver.imgs": ["*.gif", "*.png"]},
    include_package_data=True,
    entry_points={"console_scripts": ["programver=programver.__main__:main"]},
)
