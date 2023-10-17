# filename: number_output.py

code = '''
# Open a file in write mode
file = open("number_output.txt", "w")

# Loop through numbers 1 to 100
for i in range(1, 101):
    # Write each number to the file
    file.write(str(i) + "\\n")

# Close the file
file.close()

print("Numbers 1 to 100 have been written to number_output.txt file.")
'''

# Open a file in write mode
file = open("number_output_code.py", "w")

# Write the code to the file
file.write(code)

# Close the file
file.close()

print("Python code has been saved in number_output_code.py file.")

# TERMINATE