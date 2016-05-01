#####################################
#                 1                 #
#####################################

import unicodecsv

def read_csv(file_name):
    with open(file_name, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

## Read in the data from daily_engagement.csv and project_submissions.csv
## and store the results in the below variables.
## Then look at the first row of each table.

daily_engagement = read_csv("DATA/daily_engagement.csv")
project_submissions = read_csv("DATA/project_submissions.csv")

print daily_engagement[0]
print project_submissions[0]
