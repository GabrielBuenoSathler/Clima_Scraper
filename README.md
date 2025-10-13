This project is a Python web scraper that collects weather data from a public API (HG Brasil) and automatically stores the information in a PostgreSQL database.
The system performs HTTP requests, processes the results (such as maximum temperature, date, and city name), and executes secure insertions using the psycopg2 driver.
