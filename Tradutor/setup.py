from setuptools import find_packages
from cx_Freeze import setup, Executable


options = {
    'build_exe': {
        'includes': [
            'cx_Logging', 'idna',
        ],
        'packages': [
            'asyncio', 'flask', 'jinja2', 'dash', 'plotly', 'waitress'
        ],
        'excludes': ['tkinter']
    }
}

executables = [
    Executable('server.py',
               base='console',
               targetName='halliburton_dash_rig.exe')
]

setup(
    name='halliburton_dash_rig',
    packages=find_packages(),
    version='0.4.0',
    description='rig',
    executables=executables,
    options=options
)