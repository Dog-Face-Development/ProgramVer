from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
	name='programver',
	version='1.9.0',
    description="A Python version of Microsoft's 'winver', built to be customizable, and to show copyright info and licenses.",
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
    ],
    keywords='program version windows winver microsoft license gui',
    url='https://github.com/Dog-Face-Development/ProgramVer',
    author='willtheorangeguy',
    packages=find_packages(where="imgs"),
    package_dir={"": "imgs"},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'programver=main:ProgramVer'
        ]
    },
)
