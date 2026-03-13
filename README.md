# api-data-fetcher (Python)

A simple Python tool that fetches cryptocurrency price data from an API and saves it to a CSV file.

## Features

- Fetch real-time Bitcoin prices
- Save API data to CSV
- Timestamp each data fetch
- Easy to extend for other APIs

## Technologies Used

- Python
- Requests
- Pandas

## Installation

Install dependencies:

```
pip install requests pandas
```

## Usage

Run the script:

```
python api_data_fetcher.py
```

The script will:

1. Fetch live Bitcoin price data
2. Store the data in `output_data.csv`
3. Print the result in the terminal

## Example Output

```
timestamp              BTC_USD  BTC_GBP  BTC_EUR
2026-03-13 10:40:22    67245    52104    60120
```

## Project Structure

```
api-data-fetcher
│
├── api_data_fetcher.py
├── output_data.csv
└── README.md
```

## Future Improvements

- Support multiple APIs
- Add scheduled data collection
- Export data visualization charts

## Author

Himanshu
