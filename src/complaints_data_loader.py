import csv
from collections import defaultdict
from datetime import datetime
import os
import warnings


class ComplaintsDataLoader:
    """DataLoader to read data from input file and prepares it for processing
    Attributes:
        file_path: Specifies where the input data set resides
        complaints_data: The data extracted from the input data set
    """

    def __init__(self, file_path=None):
        self.file_path = file_path  # input file
        self.complaints_data = defaultdict(lambda: defaultdict(int))  # container for the data

    def extract_data(self, record):
        """ each row in the input complaints file is stored in a dictionary data structure as {(Product,Year) : {Company:count}}
            Key Fields transformed while storing : Product - all lowercase, Company -  capital case, Year - extract the year from complaint date
        """
        if record[0] and record[1] and record[7]:
            product = str.lower(record[1])
            company = str.capitalize(record[7])
            year = datetime.strptime(record[0], '%Y-%m-%d').year
            # count of complaints on the same product made on the same year are grouped by company names
            self.complaints_data[(product, year)][company] += 1
        else:
            warnings.warn('Data in the record:--' + record + '--is not properly cleaned', RuntimeWarning)

    def load_data(self):
        """extract from the input file and store the relevant data in the dictonary"""
        if self.file_path is not None:
            if not os.path.isfile(self.file_path):
                raise FileNotFoundError('The file does not exist')

            with open(self.file_path, errors='ignore') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                # skipping header
                csv_reader.__next__()
                # process extraction
                [self.extract_data(record) for record in csv_reader]

        if not self.complaints_data:
            raise ValueError('No data to load')

        return self.complaints_data
