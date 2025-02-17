'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''
with open('student_grades.csv','r') as f:

    # collect all lines from the file
    lines = f.readlines()


    # validate file has data
    if len(lines) > 0:
        grades = []
        # iterate through each line and collect the grade
        # skipping the first 'header' line
        for line in lines[1:]:
            # split the line into a list (i.e. columns)
            row = line.split(',')

            # convert the grade to a float and add it to the list
            grades.append(float(row[3].replace('\n','')))

        avg = sum(grades) / len(grades)
#Created an output file
        with open('student_grade_differences.csv', 'w') as output:
            #Wrote a header for each of the values
            output.truncate
            output.write(f'id, first_name, last_name, grade, difference\n')
            
            #Split the values into columns
            for line in lines[1:]:
                row = line.split(',')
                grade = float(row[3].replace('\n',''))
                #Calculated the difference
                difference = grade - avg
                output.write(f'{row[0]}, {row[1]}, {row[2]}, {grade}, {difference}\n')