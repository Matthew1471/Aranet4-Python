import csv

import aranet4

# Aranet4 MAC address
device_mac = "XX:XX:XX:XX:XX:XX"

# Selection filter. Will export last 25 records
entry_filter = {
    "last": 25
}

# Fetch results
records = aranet4.client.get_all_records(
    device_mac,
    entry_filter,
    remove_empty=True # This will remove blank records, if range parameters (start,end,last) are specified
)

# Write CSV file
with open(file="aranet_history.csv", mode="w", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    header = [
        "date",
        "co2",
        "temperature",
        "humidity",
        "pressure"
    ]

    # Write CSV header
    writer.writerow(header)

    # Write CSV rows
    for line in records.value:
        row = [
            line.date.isoformat(),
            line.co2,
            line.temperature,
            line.humidity,
            line.pressure
        ]

        writer.writerow(row)
