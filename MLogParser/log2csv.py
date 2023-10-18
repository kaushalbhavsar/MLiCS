import csv
import re


#Converts Apache access logs to CSV file. 

# Regular expression to match the Apache log format
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) ".*?" "(.*?)"'
log_regex = re.compile(log_pattern)

# Define the headers for the CSV file
headers = ['IP', 'DateTime', 'Request', 'Status', 'Size', 'UserAgent']

# Create a new CSV file
with open('log_data_test.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the headers to the CSV file
    writer.writerow(headers)

    # Read the log file line-by-line
    with open('log.txt', 'r') as log_file:
        for line in log_file:
            match = log_regex.match(line)
            if match:
                # Extract the matched groups
                ip, datetime, request, status, size, user_agent = match.groups()

                # Write the extracted data to the CSV file
                writer.writerow([ip, datetime, request, status, size, user_agent])
