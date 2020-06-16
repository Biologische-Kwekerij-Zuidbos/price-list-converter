from setuptools import setup

setup(
    install_requires=[
        'pandas',
        'openpyxl',
    ],
    extras_require={
        ':sys_platform == "win32"': [
            'pywin32'
        ]
    }
)