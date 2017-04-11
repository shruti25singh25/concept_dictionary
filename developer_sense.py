filenames = ['/home/shruti/create-hindi-parser/chl_to_dmrs/sense_modified_csv/developer_data.out', '/home/shruti/create-hindi-parser/chl_to_dmrs/sense_modified_csv/sense_data.out']
with open('result.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
