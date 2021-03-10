#A school decided to replace the desks in three classrooms> Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers. The first group has 20 students and thus need 10 desks.
#The second group has 21 students so they can get with no fewer than 11 desks. 11 desks are also enough for third group
#of 22 students . So, we need 32 desks in total
first_class =int(input("Enter the number of students in first class"))
second_class =int(input("Enter the number of students in second class"))
third_class =int(input("Enter the number of students in third class"))
total_students = first_class+second_class+third_class
number_of_desks = total_students//2
remaining = total_students%2
least_number_of_desks= number_of_desks+remaining
print(f"The least number of desks required is {least_number_of_desks}")
