CSV Audit Log Processor
Overview
This Python script processes audit logs stored in a CSV file, extracts useful fields from the AuditData column (which contains JSON data), and outputs the cleaned, human-readable data into a new CSV file.

How It Works
The script performs the following steps:

Reads a CSV file containing audit logs.
Parses the AuditData column (which is in JSON format) to extract specific fields of interest.
Removes unwanted fields from the AppAccessContext section of the AuditData.
Outputs a new CSV file with the processed and human-readable data.
Key Features:
Extracts important fields such as CreationTime, Operation, UserId, ClientIP, Platform, and File/Message.
Flattens the AppAccessContext, but only keeps the ClientAppName while discarding fields like AADSessionId, CorrelationId, TokenIssuedAtTime, and UniqueTokenId.
Automatically removes the original AuditData column and outputs the processed data to a new CSV file.
File Structure:
Input: The input is a CSV file with an AuditData column that contains JSON data along with other fields.
Output: The output is a new CSV file with clean, human-readable columns.
How to Use
Install Required Libraries: You need to have Python installed, along with the pandas library. You can install the necessary dependencies with:

Copy code
pip install pandas
Set Input and Output File Paths: You can specify the input and output file paths by editing the following lines in the script:

python
Copy code
input_file_path = "path/to/your/input_audit_log.csv"
output_file_path = "path/to/your/output_readable_audit_log.csv"
To point the script to a different CSV file, simply change the input_file_path and output_file_path values to your desired file paths.

Run the Script: Once you have set the file paths, run the script:

Copy code
python process_audit_log.py
The script will generate a new, human-readable CSV file at the specified output path.

Changing to a Different CSV File
To process a different CSV file, you need to:

Update the input_file_path with the full path of your new CSV file.
Optionally, update the output_file_path if you want to save the processed file with a different name or location.
For example, to process a file called new_audit_log.csv located in a generic folder:

python
Copy code
input_file_path = "path/to/your/new_audit_log.csv"
output_file_path = "path/to/your/output_readable_new_audit_log.csv"
After updating the file paths, rerun the script and it will process the new file accordingly.
