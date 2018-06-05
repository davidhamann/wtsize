from setuptools import setup

setup(
    name='wtsize',
    version='0.1.0',
    author='David Hamann',
    author_email='dh@davidhamann.de',
    packages=['wtsize'],
    include_package_data=True,
    install_requires=['requests', 'docopt'],
    entry_points={
        'console_scripts': ['wtsize=wtsize.wtsize:main']
    }
)
