import csv
import numpy as np

ROWS = 10000

increment = 0

with open('flight_vals.csv', mode='w') as csv_file:
    writer = csv.writer(
        csv_file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['heading_deg', 'speed_knots', 'pressure_Pa',
                     'altitude_ft', 'roll_deg', 'pitch_deg'])
    for _ in range(ROWS):
        writer.writerow([180 + 180 * np.sin(increment / 25),
                         80 + 80 * np.sin(increment / 600),
                         1000 + 3 * np.sin(increment / 50),
                         1250 + 1250 * np.sin(increment / 250),
                         180 * np.sin(increment / 150),
                         180 * np.sin(increment / 300)])
        increment += 1


print("Done")
