from setuptools import find_packages, setup


setup(
    name='flask_app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pandas',
        'openpyxl',
        'flask',
        'flask-sqlalchemy',
        'datetime',
        'flask-wtf'
    ],
)
