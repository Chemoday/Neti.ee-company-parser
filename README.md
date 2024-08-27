# Neti.ee Company Parser

Neti.ee Company Parser is a script for parsing company information from the Estonian website directory [Neti.ee](https://www.neti.ee/).

## Functionality

The script is designed to collect data on companies presented on the Neti.ee website. It allows you to extract the company name, address, phone number, as well as the URL of the company's website.

## Installation

To work with the script, you need to install Python and several libraries.

1. Clone the repository:
```bash
git clone https://github.com/visualGravitySense/Neti.ee-company-parser.git
cd Neti.ee-company-parser
```

2. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script, specifying the necessary command line parameters. For example:

```bash
python parser.py
```

### Command line arguments

- `--category` - Category of companies to parse (e.g. "Business", "Healthcare").
- `--output` - Output file name to save data to (default is `output.csv`).

### Run examples

Parsing the "Business" category and saving the results to `business_companies.csv`:

```bash
python parser.py --category "Business" --output business_companies.csv
```

## Usage examples

Example output:

| Company name | Address | Phone | Website |
|-------------------|--------------------|-------------|-----------------------|
| Example Company | Tallinn, ul. Example 1 | +372 123456 | https://example.com |

## Contribute

If you want to contribute to the project, please follow these instructions:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push your changes to the repository (`git push origin feature-branch`).
5. Create a Pull Request.

## Contact

If you have any questions or suggestions, you can contact me via email: `dmitri.gornakov@gmail.com`.
