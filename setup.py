from setuptools import setup

with open("README.md", "r") as ld:
    long_description = ld.read()

setup(
    name='wtsize',
    version='0.1.0',
    author='David Hamann',
    author_email='dh@davidhamann.de',
    description='WTSize let\'s you check the size of a remote file without downloading it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/davidhamann/wtsize',
    packages=['wtsize'],
    include_package_data=True,
    install_requires=['requests', 'docopt'],
    entry_points={
        'console_scripts': ['wtsize=wtsize.wtsize:main']
    },
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    )
)
