import setuptools

setuptools.setup(
    name='Brazilian-Forecast.io',
    version='0.0.1',
    author='Antonio Campos',
    author_email='tonyldo@gmail.com',
    packages=['brazilianforecast'],
    url='http://pypi.python.org/pypi/BrazilianForecastIO/',
    license='LICENSE',
    description='Friendly Python API for Brazilian Forecast powered by CPTEC-INPE.',
    long_description=open('README.md').read(),
    install_requires=[
        "aiohttp",
        "geopy",
        "requests",
        "astral"
    ],
)