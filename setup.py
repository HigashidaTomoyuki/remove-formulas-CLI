from setuptools import find_packages, setup

setup(
    name='rmformulas',
    version='0.1',
    description='Remove formulas CLI',
    author='HigashidaTomoyuki',
    license='MIT',
    packages=find_packages("rmformulas"),
    package_dir={'': "rmformulas"},
    py_modules=["rmformulas"],
    install_requires=[
        'Click',
        'Pillow',
        'openpyxl'
    ],
    entry_points={
        "console_scripts": [
            "rmformulas=rmformulas:cli"
        ]
    }
)
