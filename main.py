def parse_lines(filename):
    parsed_data = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split()
            first_name = fields[0]
            last_name = fields[1]
            age = fields[2]
            status = fields[3]

            record = {'FirstName': first_name, 'LastName': last_name, 'age': age, 'status': status}
            parsed_data.append(record)
    return parsed_data


def check_positive(fields) -> str:
    positive_count = 0
    for i in range(3):
        person = fields[i]
        if person['status'] == 'Positive':
            positive_count += 1
    return f"There are {positive_count} positive characters"


lines = parse_lines('info.txt')
positive = check_positive(lines)
file = open('filtered.txt', 'w')
file.write(positive)
