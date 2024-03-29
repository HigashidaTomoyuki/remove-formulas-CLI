from setuptools import find_packages, setup

readme = ""
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="rmformulas",
    version="1.0.1",
    description="Remove formulas CLI",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="HigashidaTomoyuki",
    license="MIT",
    url="https://github.com/HigashidaTomoyuki/remove-formulas-CLI",
    packages=find_packages(exclude=["tests"]),
    install_requires=["Click==7.1.2", "Pillow==8.2.0", "openpyxl==3.0.3"],
    entry_points={"console_scripts": ["rmformulas=rmformulas.rmformulas:cli"]},
)
