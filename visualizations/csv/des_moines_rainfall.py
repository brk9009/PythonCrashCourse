import csv

from matplotlib import pyplot as plt 

filename="des_moines_rainfall.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_record = next(reader)

    dates, rainfalls = [], []
    for row in reader:
        try:
            current_date = row[0]
            rainfall = float(row[2])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

# Plot Des Moines data
fig = plt.figure(dpi=128, figsize=(12,7))
plt.plot(dates, rainfalls, c='blue', alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)

# Format plot
title = "Daily rainfall - March 2019\nDes Moines, IA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Rainfall(in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()