import time
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urls import *

data = [["URL", "Title", "Screening type", "Date", "Time", "Venue", "City"]]

def main():
    # Create CSS selectors
    css_select_title = ".sd_film_description h2.sd_textuppercase"
    css_select_screenings_container = (
        ".screening_sateligh_timing .screening_sateligh_timing_column_inner"
    )
    css_select_screenings = ".sd_screening_details"
    css_select_date = ".sd_film_desc_time"
    css_select_type = ".sd_film_type_text"
    css_select_venue = ".sd_film_desc_avail"
    css_select_city = ".sd_film_desc_city"

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")

    # Create instance of Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        for url in urls:
            # Open page
            print("\n==========\n")
            print(f'🔗 Opening {url}')
            driver.get(url)

            # Wait for JavaScript to execute
            time.sleep(2)

            # Get title
            title_element = driver.find_element(By.CSS_SELECTOR, css_select_title)
            title = title_element.get_attribute("textContent").strip()
            print(f'👀 Found {title}')

            # Get screenings container
            screenings_container_element = driver.find_element(
                By.CSS_SELECTOR, css_select_screenings_container
            )

            # Iterate through each screening
            for screening in screenings_container_element.find_elements(
                By.CSS_SELECTOR, css_select_screenings
            ):
                # Get type
                type_element = screening.find_element(By.CSS_SELECTOR, css_select_type)
                type = type_element.get_attribute("textContent").strip()
                print(f'\n🎥 {type}')

                # Get date and time
                timestamp_element = screening.find_element(
                    By.CSS_SELECTOR, css_select_date
                )
                timestamp = timestamp_element.get_attribute("textContent")
                split = timestamp.split(",", 1)
                day = split[0].strip()
                start_time = split[1].strip()
                print(f'📅 {day} at {start_time}')

                # Get location
                venue_element = screening.find_element(
                    By.CSS_SELECTOR, css_select_venue
                )
                venue = venue_element.get_attribute("textContent").strip()
                city_element = screening.find_element(By.CSS_SELECTOR, css_select_city)
                city = city_element.get_attribute("textContent").strip()
                print(f'📍 {venue} in {city}')

                data.append(
                    [
                        url,
                        title,
                        type,
                        day,
                        start_time,
                        venue,
                        city,
                    ]
                )

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close driver
        driver.quit()

        # Output CSV
        timestamp = time.time()
        timestamp_formatted = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d-%H:%M:%S')
        csv_file_path = f'output-{timestamp_formatted}.csv'
        with open(csv_file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
        print(f'\n\n✅ CSV file "{csv_file_path}" has been created')


if __name__ == "__main__":
    main()
