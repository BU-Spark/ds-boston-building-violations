import csv

csv_file_path = "public_works_violations_2019_to_present.csv"

with open(csv_file_path, 'w', newline='') as new_csv_file:
    with open('Public_Works_Violations_Dataset.csv', 'r') as f:
        csv_file = csv.reader(f)
        csv_writer = csv.writer(new_csv_file)

        header = next(csv_file)
        csv_writer.writerow(header)
        for row in csv_file:
            dttm = row[3]
            if row[3] == '':
                continue
            date_and_time = dttm.split(' ')
            year = date_and_time[0].split('-')[0]
            if int(year) >= 2019:
                csv_writer.writerow(row)