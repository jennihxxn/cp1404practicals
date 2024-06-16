"""
CP1404/CP5632 Practical
"""
FILENAME = "subject_data.txt"
def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        data.append(parts)  # Append the parts to the data list
    input_file.close()
    return data

def display_subject_details(data):
    """Display subject details."""
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]} and has {subject_data[2]} students")

main()