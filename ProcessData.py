#ProcessData.py
#Name:Gavin Grow
#Date:3/28/26
#Assignment:process data

import csv

def main():
    input_path = "names.dat"
    output_path = "StudentList.csv"

    with open(input_path, 'r', encoding='utf-8') as inFile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outFile:
        writer = csv.writer(outFile)
        writer.writerow(["LastName", "FirstName", "UserID", "Major-Year"])

        for line in inFile:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) < 7:
                continue

            first_name = parts[0]
            last_name = parts[1]
            student_id = parts[3]
            school_year = parts[5]
            major = " ".join(parts[6:])

            user_id = make_userid(first_name, last_name, student_id)
            major_year = make_major_year(major, school_year)

            writer.writerow([last_name, first_name, user_id, major_year])


def make_userid(first, last, student_id):
    clean_id = ''.join(ch for ch in student_id if ch.isdigit())
    last3 = clean_id[-3:] if len(clean_id) >= 3 else clean_id.zfill(3)

    last_clean = ''.join(ch for ch in last if ch.isalpha())
    if len(last_clean) < 5:
        last_clean = last_clean + 'x' * (5 - len(last_clean))
    else:
        last_clean = last_clean[:5]

    return f"{first[0].lower()}{last_clean.lower()}{last3}"


def make_major_year(major, year):
    major_word = major.split()[0] if major else ""
    major_code = major_word[:3].upper().ljust(3, 'X')

    year_map = {
        'Freshman': 'FR',
        'Sophomore': 'SO',
        'Junior': 'JR',
        'Senior': 'SR'
    }
    year_code = year_map.get(year, year[:2].upper())

    return f"{major_code}-{year_code}"


if __name__ == '__main__':
    main()

