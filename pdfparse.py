from tabula import convert_into
import glob
import csv
import os

with open('output.csv', 'wt') as out:
    writer = csv.writer(out, dialect='excel', delimiter=',', lineterminator='\n')
    writer.writerow(['FILENAME', 'TYPE', 'DOC. # / REV #', 'TITLE', 'EFFECTIVE DATE'])
    # convert the pdf table content into csv files
    for f in glob.glob('**/*.pdf', recursive=True):
        print('parsing file: '+f)

        # using tabula-py, extract the table contents of the pdf and out to tmp.csv
        convert_into(f, 'tmp.csv', output_format='csv',
                     java_options='-Dsun.java2d.cmm=sun.java2d.cmm.kcms.KcmsServiceProvider')
        with open('tmp.csv', 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            # first element of the saved rows is the filename
            saved_rows = []
            found_last = False
            for row in reader:
                saved_rows.append(row)
                if 'PAGE' in row:
                    break

            # values for each column of the new row
            filename = f
            doctype = saved_rows[0][0]
            docrev_num = ''
            name = ''
            date = ''
            for r in saved_rows:
                if docrev_num == '' and 'DOC. # / REV #' in r:
                    docrev_num = r[r.index('DOC. # / REV #')+1]
                if date == '' and 'EFFECTIVE DATE' in r:
                    date = r[r.index('EFFECTIVE DATE')+1]

                # special handling for standard operating procedure type
                if doctype == 'STANDARD OPERATING':
                    if doctype not in r and 'PROCEDURE' not in r:
                        name = name + ' ' + r[0]
                else:
                    if doctype not in r and not r[0] == doctype:
                        name = name + r[0] + ' '
            if doctype == 'STANDARD OPERATING':
                doctype = 'STANDARD OPERATING PROCEDURE'

            new_row = [filename.strip(), doctype.strip(), docrev_num.strip(), name.strip(), date.strip()]

            # add the new row to the array of rows
            writer.writerow(new_row)

if os.path.exists('tmp.csv'):
    os.remove('tmp.csv')
