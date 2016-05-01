#####################################
#                 2                 #
#####################################

## Find the total number of rows and the number of unique students (account keys)
## in each table.
from fix_data_types import *

def get_row(table, key_name=None):
    if key_name:
        uni_set = set()
        for item in table:
            uni_set.add(item[key_name])
        return len(table), len(uni_set)
    else:
        return 0, 0

enrollment_num_rows = get_row(enrollments, 'account_key')[0]
enrollment_num_unique_students = get_row(enrollments, 'account_key')[1]

engagement_num_rows = get_row(daily_engagement, 'acct')[0]
engagement_num_unique_students = get_row(daily_engagement, 'acct')[1]

submission_num_rows = get_row(project_submissions, 'account_key')[0]
submission_num_unique_students = get_row(project_submissions, 'account_key')[1]
