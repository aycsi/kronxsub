import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event
from datetime import datetime
import os

<<<<<<< HEAD
URL = "" 
=======
URL = "https://schema.oru.se/setup/jsp/Schema.jsp?startDatum=idag&intervallTyp=m&intervallAntal=12&sokMedAND=true&schemaTyp=SchemaOptimal&forklaringar=true&resurser=k.DT118G-H5016H25-&sprak=SV"

>>>>>>> 4ea92ee8d8dccf72c0ed59275381f699d854a75a
def fetch_schedule():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'schemaTabell'})

    if not table:
<<<<<<< HEAD
        print("no schedule table found.")
=======
>>>>>>> 4ea92ee8d8dccf72c0ed59275381f699d854a75a
        return []

    events = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) < 5:
            continue

        date_str = cells[0].get_text(strip=True)
        time_str = cells[1].get_text(strip=True)
        title = cells[3].get_text(strip=True)
        location = cells[4].get_text(strip=True)

<<<<<<< HEAD
=======
        if " - " not in time_str:
            continue

>>>>>>> 4ea92ee8d8dccf72c0ed59275381f699d854a75a
        try:
            start_time, end_time = time_str.split(" - ")
            start_dt = datetime.strptime(f"{date_str} {start_time}", '%Y-%m-%d %H:%M')
            end_dt = datetime.strptime(f"{date_str} {end_time}", '%Y-%m-%d %H:%M')
<<<<<<< HEAD
        except Exception as e:
            print(f"skipping invalid row: {e}")
=======
        except Exception:
>>>>>>> 4ea92ee8d8dccf72c0ed59275381f699d854a75a
            continue

        event = Event()
        event.name = title
        event.begin = start_dt
        event.end = end_dt
        event.location = location
        events.append(event)

    return events

def generate_ics(events, path):
    calendar = Calendar()
    for event in events:
        calendar.events.add(event)
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(calendar)

if __name__ == "__main__":
    events = fetch_schedule()
<<<<<<< HEAD
    if events:
        os.makedirs("docs", exist_ok=True)
        generate_ics(events, "docs/oru_schedule.ics")
        print(f"done {len(events)} events.")
    else:
        print("no events.")
=======
    os.makedirs("docs", exist_ok=True)
    generate_ics(events, "docs/oru_schedule.ics")
    print(f"done {len(events)} events")
>>>>>>> 4ea92ee8d8dccf72c0ed59275381f699d854a75a
