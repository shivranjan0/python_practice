#Log File Analyzer:
#Write a script to parse a log file and summarize the number of errors and warnings.

Error_count = 0
warning_count = 0
#Open the file
with open('log.txt', 'r') as file:
    for line in file:
        if 'Error' in line:
            Error_count += 1
        elif 'warning' in line:
            warning_count += 1
    print(f'Errors: {Error_count}')
    print(f'Warnings: {warning_count}')
