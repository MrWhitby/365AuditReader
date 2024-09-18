import csv
import json
import pandas as pd


def process_audit_data(audit_data):
    try:
        # Convert the audit data from string to JSON
        audit_json = json.loads(audit_data)

        # Extract fields of interest
        app_access_context = audit_json.get('AppAccessContext', {})

        # Extracting key fields from the audit JSON, excluding the unwanted fields
        readable_audit_data = {
            'CreationTime': audit_json.get('CreationTime', ''),
            'Operation': audit_json.get('Operation', ''),
            'UserId': audit_json.get('UserId', ''),
            'ClientIP': audit_json.get('ClientIP', ''),
            'Platform': audit_json.get('Platform', ''),
            'File/Message': audit_json.get('SourceFileName', audit_json.get('Item', {}).get('Subject', '')),

            # Flattening AppAccessContext fields excluding the unwanted ones
            'ClientAppName': app_access_context.get('ClientAppName', '')
        }
        return readable_audit_data
    except Exception as e:
        return {'Error': str(e)}


def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        rows = []
        for row in reader:
            audit_data = process_audit_data(row['AuditData'])
            row.update(audit_data)
            rows.append(row)

    # Convert to DataFrame for easier handling
    df = pd.DataFrame(rows)

    # Drop the original AuditData column
    df.drop(columns=['AuditData'], inplace=True)

    # Save to a new CSV file
    df.to_csv(output_file, index=False)

    return df


# Input and output file paths (adjust the path as necessary)
input_file_path = "C:/Users/jacob/Downloads/83f6482e-6852-4b9e-9c10-6d60ceeea9fa.csv"
output_file_path = "C:/Users/jacob/Downloads/readable_audit_log.csv"

# Process the CSV file and make it human-readable
df = process_csv(input_file_path, output_file_path)

# Display the resulting DataFrame (optional, for viewing in a Python environment)
print(df)
