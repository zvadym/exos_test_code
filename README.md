## Python Code Task

**Estimated development:**

3-4 Hrs. If the task takes longer than expected, stop at any point when you feel comfortable with
the code.

**Important Notes:**

Please note that you will be judged on the overall quality of the code (readability, best practice
compliance, etc.) and approach of the solution. It IS OKAY to use third party packages as it is a
common practice in Django. Do NOT use built in admin.

**Specification:**

The task is made up of 5 parts plus an optional task.

1. Set up a basic django 1.9 installation using a sqlite database in the same folder as the
source
2. Add two fields to the User model using a migration:
 - birthday field of type date
 - random number field of type integer that is assigned a value from 1-100 on
creation
3. Create views for listing all users, viewing, adding, editing and deleting a single user
4. Create two template tags:
 - A tag that will display "allowed" if the user is > 13 years old otherwise display
"blocked"
 - A tag that will display the BizzFuzz result of the random number that was
generated for the user. The BizzFuzz specification is that for multiples of three
print "Bizz" instead of the number and for the multiples of five print "Fuzz". For
numbers which are multiples of both three and five print "BizzFuzz"
 - Add a column to the list view after the birthday column that uses the
allowed/blocked tag
 - Add a column to the list view after the random number column that uses the
BizzFuzz tag
5. Unit test what you feel is appropriate to test.

Time permitting, create a download link on the list view that would allow the list to be exported
to excel.


| Username | Birthday   | Eligible | Random Number | BizzFuzz |
|----------|------------|----------|---------------|----------|
| user1    | 1/1/2013   | blocked  | 40            | Fuzz     |
| user2    | 12/12/1988 | allowed  | 66            | Bizz     |
| user3    | 4/5/1975   | allowed  | 41            | 41       |
| user4    | 4/5/2017   | blocked  | 30            | BizzFuzz |