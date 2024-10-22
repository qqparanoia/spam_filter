def read_classification_from_file(file_path: str):
    result = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split()
            result[data[0]] = data[1]
    return result

if __name__ == '__main__':
    data = read_classification_from_file('1/!truth.txt')
    for key, value in data.items():
        print( key, value)