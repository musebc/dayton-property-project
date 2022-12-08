import csv

with open('Delq_20221130.csv', newline='') as delinquent_file:
    header = [h.strip() for h in delinquent_file.readline().split(',')]
    delinquent_file_reader = csv.DictReader(delinquent_file, fieldnames=header)
    row_counter = 0
    value_index = 0
    owed_index = None
    valid = 0
    for row in delinquent_file_reader:
        home_value = row.get("ASMTTOTAL")
        tax_owed = row.get("NETDELQ")
        if home_value and tax_owed and float(tax_owed) > float(home_value):
            valid += 1

        row_counter += 1

    print(valid)


