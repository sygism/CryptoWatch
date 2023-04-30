# CryptoWatch

CryptoWatch is a Qt6 based GUI program for cryptocurrency price monitoring and analysis.
The pricing data is scraped using <a href="https://alphavantage.co/">AlphaVantage</a> Python API.
The application is capable of calculating and displaying SMA, trend line and resistance line plots alongside
the price data of the selected cryptocurrency. The user can search the local database for supported currencies and add
coins as their favourites.

## Getting Started

Python3, aswell as the required packages, are needed to execute the program.

To run the program from **bash**/**cmd** etc.,

<code>python3 main.py</code>

### Prerequisites

Requirements for the software and other tools to build, test and push 
- <a href="https://pypi.org/project/PyQt6/">PyQt6</a>
- <a href="https://pypi.org/project/pandas">pandas</a>
- <a href="https://pypi.org/project/numpy/">numpy</a>
- <a href="https://pypi.org/project/dotenv/">dotenv</a>

An AlphaVantage API key is required for running the program, it must be copied into the
.env file:
<code>ALPHA_VANTAGE_API_KEY=<YOUR_API_KEY_GOES_HERE></code>

## Authors

  - **Markus Erik Sügis** - 
    [sygism](https://github.com/sygism)

## License

This project is not licensed and is free to be used in any way.
