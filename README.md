# Neti.ee Company Parser

This project is a web scraping tool designed to extract and organize company data from the Estonian web directory, Neti.ee. The parser automates the process of gathering information such as registration codes, VAT numbers, addresses, and contact details from Neti.ee's business listings, and stores the data in a structured format using a database or CSV files.

## Project Overview

The Neti.ee Company Parser is built to efficiently scrape business information from the Neti.ee website. It leverages Selenium for web automation, Peewee for database management, and Python's multiprocessing capabilities to handle large-scale data scraping and parsing tasks concurrently.

### Key Features

- **Automated Web Scraping:** Uses Selenium WebDriver to automate the browsing and extraction of company data from Neti.ee.
- **Multithreading Support:** Utilizes Python's `multiprocessing` library to enhance performance by processing multiple pages concurrently.
- **Data Storage:** Extracted data is stored in an SQLite database using the Peewee ORM or can be exported to CSV files for further analysis.
- **Configurable:** Supports different operating systems (Windows and Linux) and can be configured with various service arguments and capabilities for Selenium.
- **Error Handling:** Includes basic exception handling to manage errors during web scraping and database operations.

### Getting Started

To run the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Neti.ee-company-parser.git
   cd Neti.ee-company-parser
   ```

2. **Install Dependencies:**
   Make sure to have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Settings:**
   Adjust the configuration settings in the `config.py` file, such as the operating system type and PhantomJS path.

4. **Run the Parser:**
   Execute the main script to start parsing:
   ```bash
   python main.py
   ```

### Prerequisites

- Python 3.x
- Selenium WebDriver
- PhantomJS (for headless browsing)
- Peewee (for database operations)
- Pandas (for CSV export)

### Project Structure

- `Parser.py`: Contains the main parsing logic and web scraping functions.
- `Database.py`: Handles database connections and operations using Peewee ORM.
- `Logger.py`: A simple logger for tracking scraping progress and errors.
- `CompanyStruct.py`: Defines the `CompanyStruct` class for managing company data objects.
- `config.py`: Configuration file for setting up scraping parameters and Selenium capabilities.
- `main.py`: Entry point to start the parsing process.

### Example Usage

To scrape company data from a specific Neti.ee category:

1. Open `main.py`.
2. Update the `url` variable with the desired category URL from Neti.ee.
3. Run the script to start scraping and saving the data.

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.


## Contact

If you have any questions or suggestions, you can contact me via email: `dmitri.gornakov@gmail.com`.
