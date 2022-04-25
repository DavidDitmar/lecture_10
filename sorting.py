import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for key, value in row.items():
                if not key in data:
                    data[key] = []
                data[key].append(int(value))
    return data




def selection_sort(number_array, direction="ascending"):
    n = len(number_array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if direction == "ascending":
                if number_array[j] < number_array[min_idx]:
                    min_idx = j
            elif direction == "descending":
                if number_array[j] > number_array[min_idx]:                     #staci jen zmenit znamenko
                    min_idx = j

        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]

    return number_array








def main():
    data = read_data("numbers.csv")
    #print(data)
    sorted_array = selection_sort(data["series_1"], "descending")
    print(sorted_array)


if __name__ == '__main__':
    main()
