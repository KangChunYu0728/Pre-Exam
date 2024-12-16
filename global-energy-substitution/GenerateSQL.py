import os
import csv

# Paths
csv_folder = "/Users/davidkang/Desktop/HfT Stuttgart/Business Intelligence/Pre Exam/BI - Pre Exam"  # Folder containing your CSV files
output_file = "/Users/davidkang/Desktop/HfT Stuttgart/Business Intelligence/Pre Exam/BI_Pre_Exam_Dump.sql"  # Self-contained SQL file

# Open the output SQL file for writing
with open(output_file, "w") as dump:
    # Write the database creation command
    dump.write("CREATE DATABASE IF NOT EXISTS BI_Pre_Exam_DB;\n")
    dump.write("USE BI_Pre_Exam_DB;\n\n")

    # Process each CSV file in the folder
    for file in os.listdir(csv_folder):
        if file.endswith(".csv"):  # Ensure it's a CSV file
            table_name = os.path.splitext(file)[0]  # Table name from the file name
            csv_file_path = os.path.join(csv_folder, file)

            # Read the CSV file
            with open(csv_file_path, "r", encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader)  # Get column names

                # Write CREATE TABLE statement
                dump.write(f"CREATE TABLE `{table_name}` (\n")
                dump.write(",\n".join([f"    `{col}` VARCHAR(255)" for col in headers]))
                dump.write("\n);\n\n")

                # Write INSERT INTO statements
                for row in reader:
                    # Escape single quotes in each value
                    escaped_values = [value.replace("'", "''") for value in row]  # Escape single quotes by doubling them
                    # Join the escaped values and format the insert statement
                    values = ", ".join([f"'{value}'" for value in escaped_values])
                    dump.write(f"INSERT INTO `{table_name}` ({', '.join(headers)}) VALUES ({values});\n")
                dump.write("\n")

print(f"Self-contained SQL file created: {output_file}")
