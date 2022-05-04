from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()
	
setup( 
    name="hello_world_olegk",
	version="0.0.1",
	author="Oleg K",
	author_email="ok@pochta.pochta",
	description="A Hello World package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com",
	packages=find_packages(),
	install_required = [
		'Flask=2.1.2'
	],
	python_requires='>=3.10',
)
# twine upload  dist/*
#Зависало на вводе пароля в cmd, в powershell строка ввода даже не появилась(