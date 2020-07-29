#!/usr/bin/env python
import os
import sys
from complaints_data_loader import ComplaintsDataLoader
from complaints_data_reporter import ComplaintsDataReport

file_dir = os.path.dirname(os.path.realpath('__file__'))

# Get input and output file
if len(sys.argv) < 3:
    sys.stderr.write("Usage: python {} path_to_input_file path_to_output_file\n".format((sys.argv[0])))
    sys.exit(-1)
if not os.path.exists(sys.argv[1]):
    sys.stderr.write("ERROR: Input file {} was not found!\n".format((sys.argv[1])))
    sys.exit(-1)

input_file = os.path.join(file_dir, sys.argv[1])
output_file = os.path.join(file_dir, sys.argv[2])

print('Extracting the data...')
extracted_data = ComplaintsDataLoader(input_file).load_data()

print('Writing the report data...')
report_data = ComplaintsDataReport(output_file)
report_data.set_report(extracted_data)
report_data.write_report()

print('Report data is available in ', output_file)
