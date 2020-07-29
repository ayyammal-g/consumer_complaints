# Consumer Complaints

## Table of Contents
1. [Problem](README.md#problem)
1. [Hacking the Problem](README.md#hacking-the-problem)
1. [Instructions](README.md#instructions)
1. [Repo directory structure](README.md#repo-directory-structure)
1. [Testing your code](README.md#testing-your-code)

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies. 

**For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

## Hacking the challenge

To solve this challenge, I choose python 3.8.2. 

I break down the problem into two important tasks.

1. To Read the dataset and extract the product, year and company reported in each consumer complaint.
2. Aggregate the extracted data for each product and year to find
        *total number of complaints
        *number of companies receiving the complaints
        *Highest percentage of complaints directed against a single company
        
The former task is accomplished by ComplaintsDataLoader class in complaints_data_loader.py while the later task is accomplished by ComplaintsDataReport class in complaints_data_reporter.py

## complaints_data_loader:
Given the input file, load_data() method of ComplaintsDataLoader class will load the data in the dictionary. For large data sets, the challenge was to find a better data structure to store the data. As there is a need to hash based on Product and Year Dictionary found to be well serve the purpose.
   After deciding to use dictionaries, I checked the performances of standard dict, defaultdict and Counter from collections for dealing with the sample data set.
   defaultdict performed better and so I choose choosing defaultdict. The input file is transformed into nested dictionary as,
                    {(Product, Year) : {Company1 : no_of_complaints,...}}
1. All Product names are modified as lower-case
2. To be case insensitive, All Company names uniformly represented as modied captilized case. 

## complaints_data_reporter:
ComplaintsDataReport class has method set_report to aggregate the extracted data. 
       1. Total complaints - Sum(values of inner dictionary company corresponding to the top level dictionary with the (product,year) key).
       2. Count of companies with atleast 1 complaint - length of company keys corresponding to the top level dictionary with (product,year) key.
       3. Highest Percentage of complaints against a company - max(complaints for a company) /Total complaints * 100 for each (product,year) key.
       
 Once the report data is set, a call to write_data method writes the data to the output file.
 
 ## complaints_analytics:
 This the main python file called from run.sh. It has calls to read, extract and write data through complaints_data_loader and complaints_data_reporter


## Repo directory structure
The top-level directory structure for my repo looks like the following:

    ├── README.md
    ├── run.sh
    ├── src
    │   └── consumer_complaints.py
    ├── input
    │   └── complaints.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── tests
            └── test_1
            |   ├── input
            |   │   └── complaints.csv
            |   |__ output
            |   │   └── report.csv
            ├── your-own-test_1
                ├── input
                │   └── complaints.csv
                |── output
                    └── report.csv

## Testing:

Unit testing is done by moving the input csv files to the input folder in my local machine and output files in the output folder. The generated csv output file is also tested manually by  applying necessary aggregate functions in spreadsheet.The sample input file given in the TestSuite is also tested by changing the input and output file paths in run.sh

During development, a lot of testing time spent on the performance testing to decide defaultdict vs dict vs Counter.

For the modest size dataset of size approx 1 GB given in http://files.consumerfinance.gov/ccdb/complaints.csv.zip  took approximately 3 minutes to complete.

## Instructions to Execute the code:

1. .\run.sh at the command line will execute the code. 
2. As per the instructions, it is assumed that input folder will have the complaints.csv during grading. So for now, no file is kept in the input folder. So make sure input file is placed in input folder before running run.sh file.

Email if there any questions at usharajam4u@gmail.com

