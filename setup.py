from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fixx/__init__.py
from fixx import __version__ as version

setup(
	name="fixx",
	version=version,
	description="fixx",
	author="fixx",
	author_email="fixx",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
