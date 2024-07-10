
# Web Scraping and Data Extraction from Houzz.com

## Objective

The objective of this project was to extract business details from Houzz.com, including business names, contact information, and customer reviews.

## Project Setup

### Tools Used

- **Python Libraries**: Scrapy for web crawling and data extraction, `re` for regex operations.
- **Item Pipeline**: Used to clean and format extracted data.

### Initial Approach

Initially, attempts were made using tools like BeautifulSoup for web scraping. However, limitations were encountered with dynamic content and JavaScript-rendered pages on Houzz.com. This led to the adoption of Scrapy due to its efficiency in handling dynamic content and navigating multiple pages of search results.

## Lessons Learned

### Scrapy Implementation

- **Spider Setup**: Created a Scrapy spider (`HouzzSpider`) to crawl through Houzz.com pages, starting from the professionals directory.
- **Data Extraction**: Extracted URLs for individual service providers and navigated to each provider's profile page to gather detailed information.
- **Data Fields**: Extracted fields such as URL, rating, about us section, reviews, business name, phone number, website link, address, and typical job cost using XPath and CSS selectors.

### Data Cleaning and Formatting

- **Pipeline Setup**: Implemented a Scrapy pipeline (`FormatDataPipeline`) to clean and format extracted data.
- **Phone Number Formatting**: Used regex to format phone numbers into a standard format.
- **Rating and Reviews**: Converted ratings to floats and removed non-numeric characters from reviews.

### Output

The output of the data extraction process was a structured dataset containing detailed business information from Houzz.com, formatted and cleaned.

## How to Use Scrapy

### Installation

1. **Install Scrapy**: If you haven't already, install Scrapy using pip:
   <code> pip install scrapy</code>

### Running the Spider

1. **Clone the Repository**: Clone or download the repository containing the Scrapy project.

2. **Navigate to Project Directory**: Open a terminal or command prompt and navigate to the directory where your Scrapy project (`houzzSpider` in this case) is located.

3. **Run the Spider**: Use the following command to run the Scrapy spider:
   <code>scrapy crawl houzzSpider</code>
   
4. **View Output**: After the spider completes crawling and extracting data, the output will typically be saved as structured data (like JSON) or processed by pipelines according to your specifications.
