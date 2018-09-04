import os
import config
import pyexcel as pe
import csv
import logging


def main(base_dir):
    # Simply give a name to the Book class
    book = pe.get_book(file_name=os.path.join(base_dir, config.ppc_in))
    # write sheet to csv file, with name like sheet name
    with open(config.ppc_out, 'w', newline='') as csvfile:
        swriter = csv.writer(csvfile, delimiter=',', quotechar = '\"',
                                        quoting=csv.QUOTE_MINIMAL)
        # fieldnames outup csv file
        swriter.writerow(config.fieldnames)
        for sheet in book:
            try:
                bts, ip = config.bts[sheet.name]
            except KeyError as e:
                logging.error('error in configuration, no key {} in config'.format(e))
                continue
            for row in sheet:
                if type(row[0]) is int:
                    print(sheet.name, ' ',row[0], ' ', row)
                    swriter.writerow([sheet.name, row[4], row[5], bts, ip])


if __name__ == '__main__':
    # confgi logging
    logging.basicConfig(
        filename="ods2csv.log",
        level=logging.INFO,
        # format="%(asctime)s [%(name)s] [%(levelname)s]: %(message)s"
        format="%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s"
    )
    logging.info('start coverting...')
    main(os.getcwd())
