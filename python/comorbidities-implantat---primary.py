# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"7936000","system":"readv2"},{"code":"7936500","system":"readv2"},{"code":"7936511","system":"readv2"},{"code":"7936600","system":"readv2"},{"code":"7936700","system":"readv2"},{"code":"7936800","system":"readv2"},{"code":"7936900","system":"readv2"},{"code":"7936C00","system":"readv2"},{"code":"7936D00","system":"readv2"},{"code":"7936E00","system":"readv2"},{"code":"7936G00","system":"readv2"},{"code":"7936H00","system":"readv2"},{"code":"7936J00","system":"readv2"},{"code":"7936K00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('comorbidities-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["comorbidities-implantat---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["comorbidities-implantat---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["comorbidities-implantat---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
