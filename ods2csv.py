import os
# import config
import pyexcel as pe
import csv

def main(base_dir):
    # Simply give a name to the Book class
    book = pe.get_book(file_name=os.path.join(base_dir, "multiple-sheets-example.xls"))

    for sheet in book:
        # write sheet to csv file, with name like sheet name
        with open(str(sheet.name) + '.csv', 'w', newline='') as csvfile:
            swriter = csv.writer(csvfile, delimiter=',', quotechar = '\"',
                                            quoting=csv.QUOTE_MINIMAL)
            for row in sheet:
                swriter.writerow(row)


if __name__ == '__main__':
    main(os.getcwd())
