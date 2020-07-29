# Consumer Complaints

## Table of Contents
1. [Problem](README.md#problem)
1. [Hacking the Challenge](README.md#hacking-the-problem)
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

        a) total number of complaints
        
        b) number of companies receiving the complaints
        
        c) Highest percentage of complaints directed against a single company
        
The former task is accomplished by ComplaintsDataLoader class in complaints_data_loader.py while the later task is accomplished by ComplaintsDataReport class in complaints_data_reporter.py

## complaints_data_loader:
Given the input file, load_data() method of ComplaintsDataLoader class will load the data in the dictionary. Using str functions and datetime methods the input data is processed to store the data in desired form.

1. Product names are modified as lower-case.
2. Company names are uniformly represented as captilized case, to make it case insensitive.
3. Year is extracted from Date Received column using datetime.

For large data sets, the challenge was to find a better data structure to store the data. As there is a need to hash based on Product and Year, I chose dictionary data structure as this well serve the purpose.

After deciding to use dictionaries, I checked the performances of standard dict, defaultdict and Counter from collections for dealing with the sample data set. For a sample data set of 100K+ rows that are processed into 100+ size dictionary entries, defaultdict gave a faster turnaround time than the other two. So I chose defaultdict. Thus the input file is transformed into nested default dictionary as,

                                                {(Product, Year) : {Company1 : no_of_complaints for Company1,...}}
        where the tuple (Product, Year) represents key, Whose value is a default dictionary with Company name as Key and occurances of that company complaints as Value
                
         
## complaints_data_reporter:
ComplaintsDataReport class has method set_report to aggregate the extracted data. 
       1. Total complaints - Sum(values of inner dictionary company corresponding to the top level dictionary with the (product,year) key).
       2. Count of companies with atleast 1 complaint - length of company keys corresponding to the top level dictionary with (product,year) key.
       3. Highest Percentage of complaints against a company - max(complaints for a company) /Total complaints * 100 for each (product,year) key.
       
 Once the report data is set, a call to write_data method writes the data to the output file.
 
 ## complaints_analytics:
 This the main python file called from run.sh. It has calls to read, extract and write data through complaints_data_loader and complaints_data_reporter
 
## Unit Testing - unit_test_run:

Unit testing is done by using InsightTestSuite's  input/complaints.csv files and output/report.csv in the output folder. The input file's headers, The extracted data and the output file are all tested in the unit testing.

During development, a lot of testing time spent on the performance testing to decide defaultdict vs dict vs Counter.

For the modest size dataset of size approx 1 GB given in http://files.consumerfinance.gov/ccdb/complaints.csv.zip  took approximately 2 minutes to complete.
 

## Repo directory structure
The top-level directory structure for my repo looks like the following:

    ├── README.md
    ├── run.sh
    ├── src
    │   └── complaints_analytics.py
        └── complaints_data_loader.py
        └── complaints_data_reporter.py
        └── unit_test_run.py
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
            ├── test_2 
                ├── input
                │   └── complaints.csv 
                |── output
                    └── report.csv 
     
     Update:insight_testsuite--->test2: Not present - Could not push the sample 1 GB data set  used for testing as Github does not allow files larger than 100KB

## Instructions to Execute the code:

1. .\run.sh at the command line will execute the code. 
2. As per the instructions, it is assumed that input folder will have the complaints.csv during grading. So for now, no file is kept in the input folder. So make sure input file is placed in input folder before running run.sh file.

## Notes:

1. All imports are made from Python standard library
2. Passed the Test repo link given in the instructions. 

Email if there any questions at usharajam4u@gmail.com

