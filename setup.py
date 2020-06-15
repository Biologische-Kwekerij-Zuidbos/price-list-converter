from distutils.core import setup

setup(
    packages=[
        'interface',
        'text_processing'
    ],
    py_modules=[
        'pandas',
        'openpyxl',
        'win32api',
        'win32print'
    ]
)