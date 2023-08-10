# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"14AD.00","system":"readv2"},{"code":"14AN.00","system":"readv2"},{"code":"212R.00","system":"readv2"},{"code":"3272.00","system":"readv2"},{"code":"3283.00","system":"readv2"},{"code":"662S.00","system":"readv2"},{"code":"6A9..00","system":"readv2"},{"code":"7936A00","system":"readv2"},{"code":"7L1H.13","system":"readv2"},{"code":"7L1H700","system":"readv2"},{"code":"9Os..00","system":"readv2"},{"code":"9Os0.00","system":"readv2"},{"code":"9Os1.00","system":"readv2"},{"code":"9Os2.00","system":"readv2"},{"code":"G573.00","system":"readv2"},{"code":"G573000","system":"readv2"},{"code":"G573200","system":"readv2"},{"code":"G573300","system":"readv2"},{"code":"G573400","system":"readv2"},{"code":"G573z00","system":"readv2"},{"code":"G574.00","system":"readv2"},{"code":"G574000","system":"readv2"},{"code":"G574011","system":"readv2"},{"code":"G574z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('comorbidities-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["comorbidities-defibrillation---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["comorbidities-defibrillation---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["comorbidities-defibrillation---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
