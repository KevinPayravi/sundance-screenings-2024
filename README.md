# sundance-screenings-2024
## Description
This Python + Selenium script extracts film info and in-person screening times for the 2024 Sundance Film Festival.

URLs for all 2024 films are in `urls.py`. Script is in `sundance.py`.

The script outputs two CSV files at the end of execution:
* `output-films-YYYY-MM-DD-HH:MM:SS.csv`, a list of the 135 films and programs. Includes each film's category, description, tags, and credits when available.
  * Note that the individual short films that are within an encompassing program (e.g. the [Animated Short Film Program](https://festival.sundance.org/program/short-info/656e245aec4ed04276af2941)) are not parsed.
* `output-screenings-YYYY-MM-DD-HH:MM:SS.csv`, a list of in-person screenings. Includes screening type (premiere vs screening), time, venue, and city.

## Log example
<img width="800" alt="Sample output of this script showing scraped films" src="https://github.com/KevinPayravi/sundance-screenings-2024/assets/7636606/d6bd9c66-a5c8-4936-a502-db34e5261a3b">
