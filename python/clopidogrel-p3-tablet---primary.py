# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"40913","system":"gprdproduct"},{"code":"42750","system":"gprdproduct"},{"code":"489","system":"gprdproduct"},{"code":"52761","system":"gprdproduct"},{"code":"53751","system":"gprdproduct"},{"code":"54700","system":"gprdproduct"},{"code":"55161","system":"gprdproduct"},{"code":"56807","system":"gprdproduct"},{"code":"57036","system":"gprdproduct"},{"code":"58347","system":"gprdproduct"},{"code":"58448","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('clopidogrel-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["clopidogrel-p3-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["clopidogrel-p3-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["clopidogrel-p3-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
