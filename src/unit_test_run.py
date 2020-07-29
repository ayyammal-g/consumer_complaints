import unittest
import csv
import os
import re
from collections import defaultdict
from complaints_data_loader import ComplaintsDataLoader
from complaints_data_reporter import ComplaintsDataReport

class TestComplaintsAnalytics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loader = ComplaintsDataLoader('insight_testsuite/test_1/input/complaints.csv')
        cls.data_extracted = loader.load_data()
        with open(loader.file_path, 'r') as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')
            cls.records = [row for row in csv_reader]
        cls.header = cls.records[0]
        cls.data = cls.records[1:]

    def test_header(self):
        columns = ['Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue',
                   'Consumer complaint narrative', 'Company public response', 'Company',
                   'State', 'ZIP code', 'Tags', 'Consumer consent provided?',
                   'Submitted via', 'Date sent to company', 'Company response to consumer',
                   'Timely response?', 'Consumer disputed?', 'Complaint ID']

        self.assertEqual(self.header, columns)

    def test_extracted_records(self):
        test_dict = defaultdict(list)
        for row in self.data:
            test_dict['Date received'].append(row[0])
            test_dict['product'].append(row[1])
            test_dict['company'].append(row[7])

        assert all(map(re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}').match, test_dict['Date received']))
        assert all(isinstance(item, str) for item in test_dict['product'])
        assert all(isinstance(item, str) for item in test_dict['company'])

    def test_complaint_reporter(self):
        with open('insight_testsuite/test_1/output/report.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            test_output_report = [row for row in reader]

        reporter = ComplaintsDataReport()
        reporter.set_report(self.data_extracted)
        report = [list(map(str, row)) for row in reporter.get_report]
        self.assertEqual(report, test_output_report)


if __name__ == '__main__':
    unittest.main()
