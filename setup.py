from setuptools import setup

setup(
    name='random generator',
    version='0.1',
    py_modules=['rpgrandom'],
    install_requires=[
        'Click',
        'PyYAML',
        'pyreadline',
    ],
    entry_points='''
        [console_scripts]
        rpgrandom=rpgrandom:cli
    ''',
)