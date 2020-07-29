#!/usr/bin/env python
import csv


class ComplaintsDataReport:
    """A class for preparing the Consumer Complaints report in csv format
    Attributes:
        output_file_path: Path to the output file
        _report: list containing the data for reporting
    """

    def __init__(self, output_file_path=None):
        self.output_file_path = output_file_path  # Path to the output file
        self._report = []  # Output

    @property
    def get_report(self):
        return self._report

    def set_report(self, complaints_data):
        """
            Processes the complaints_data for reporting
            :param complaints_data: type: dictionary, holds the extracted data from the input file
            """
        for complaint_key, company_count in sorted(complaints_data.items()):
            total_complaints = sum(company_count.values())
            self._report.append([complaint_key[0], complaint_key[1], total_complaints, len(company_count.keys()),
                                 round(max(company_count.values()) * 100 / total_complaints)])

    def write_report(self):
        """Write the reported output into csv file."""
        if self.output_file_path is not None:
            if self._report is None:
                raise ValueError('No output to write')

            with open(self.output_file_path, "w", newline="") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerows(self._report)
