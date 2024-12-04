import csv
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        encoding = result['encoding']
        return encoding

def read_pdf_file(file_path, encoding):
    with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
        lines = f.readlines()
    return lines

def process_pdf_lines(lines):
    list_title = []
    list_profile = []
    list_description = []
    list_impact = []
    list_rationale = []
    list_remediation = []
    list_default_value = []
    list_bin = []
    list_csv_header = ["Section", "Title", "Profile Level", "Profile", "Description", "Impact", "Rationale", "Remediation"]

    bucket = list_bin

    for line in lines:
        bucket = func_define_bucket(line, bucket)
        if bucket == list_title:
            list_title.append(line.strip())
        elif bucket == list_description:
            list_description.append(line.strip())
        elif bucket == list_impact:
            list_impact.append(line.strip())
        elif bucket == list_rationale:
            list_rationale.append(line.strip())
        elif bucket == list_remediation:
            list_remediation.append(line.strip())
        elif bucket == list_default_value:
            list_default_value.append(line.strip())
        elif bucket == list_profile:
            list_profile.append(line.strip())

    return list_title, list_description, list_impact, list_rationale, list_remediation, list_default_value, list_profile

def func_define_bucket(line, bucket):
    list_bin = []  # Define la variable list_bin
    if line[:1].isnumeric() and ("(L1)" in line or "(L2)" in line or "(NG)" in line):
        bucket = list_title
    elif "Description:" in line:
        bucket = list_description
    elif "Impact:" in line:
        bucket = list_impact
    elif "Rationale:" in line:
        bucket = list_rationale
    elif "Remediation:" in line:
        bucket = list_remediation
    elif "Default Value:" in line:
        bucket = list_bin
    elif " | P a g e" in line or "Page" in line:
        bucket = list_bin
    elif "Profile Applicability:" in line:
        bucket = list_profile
    elif "Audit:" in line:
        bucket = list_bin
    elif "References:" in line:
        bucket = list_bin
    elif "CIS Controls:" in line:
        bucket = list_bin
    else:
        bucket = bucket
    return bucket

def export_data_to_csv(list_title, list_description, list_impact, list_rationale, list_remediation, list_default_value, list_profile, output_file):
    list_csv_header = ["Section", "Title", "Profile Level", "Profile", "Description", "Impact", "Rationale", "Remediation"]
    fieldnames = ['Section', 'Title', 'Profile Level', 'Profile', 'Description', 'Impact', 'Rationale', 'Remediation']
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(list_title)):
            data = {
                'Section': list_csv_header[0],
                'Title': list_title[i],
                'Profile Level': list_csv_header[2],
                'Profile': list_profile[i],
                'Description': list_description[i],
                'Impact': list_impact[i],
                'Rationale': list_rationale[i],
                'Remediation': list_remediation[i]
            }
            writer.writerow(data)

def main():
    input_file = 'archivo.pdf'
    output_file = 'policy.csv'
    encoding = detect_encoding(input_file)
    lines = read_pdf_file(input_file, encoding)
    list_title, list_description, list_impact, list_rationale, list_remediation, list_default_value, list_profile = process_pdf_lines(lines)
    export_data_to_csv(list_title, list_description, list_impact, list_rationale, list_remediation, list_default_value, list_profile, output_file)

if __name__ == '__main__':
    main()