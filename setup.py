from setuptools import setup

setup(
    name='grapple',
    entry_points={
        'console_scripts': [
            'grapple = grapple:main',
        ],
    }
)
