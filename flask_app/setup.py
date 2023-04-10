from setuptools import find_packages, setup

setup(
    name='app.py',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pandas',
        'openpyxl',
        'flask',
        'flask-sqlalchemy',
        'flask-wtf'
    ],
)