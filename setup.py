from distutils.core import setup

setup(
    install_requires=[
        'pandas',
        'openpyxl',
        'pyinstaller'
    ],
    extras_require={
        ':sys_platform == "win32"': [
            'pywin32'
        ]
    }
)