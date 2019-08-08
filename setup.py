import setuptools

setuptools.setup(
    name='Brazilian-Forecast.io',
    version='0.0.1',
    author='Antonio Campos',
    author_email='tonyldo@gmail.com',
    packages=['brazilianforecast'],
    url='http://pypi.python.org/pypi/BrazilianForecastIO/',
    license='Apache License 2.0',
    description='Friendly Python API for Brazilian Forecast powered by CPTEC-INPE.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "aiohttp",
        "geopy",
        "requests",
        "astral"
    ],
)