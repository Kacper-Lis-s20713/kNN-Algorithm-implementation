import csv
import math
import operator
import sys

# k, train-set, test-set podawane sa jako argumenty wywolania programu


# Importing data into the matrix
# For loop goes through every line in a file
# Changes first four values into a float
# And appends it to the matrix

def data_processing(file_name, t_set):
    with open(file_name, 'r') as csvfile:
        lines = csv.reader(csvfile)
        data = list(lines)
        for x in range(len(data)):
            for y in range(4):
                data[x][y] = float(data[x][y])
            t_set.append(data[x])


# Euclidean distance between two points
def e_distance(p1, p2, n_values):
    dis = 0
    for x in range(n_values):
        dis += pow((p1[x] - p2[x]), 2)
    return math.sqrt(dis)

# Predicts class
def get_prediction(t):
    class_dict = {}
    for cls in range(k):
        if t[cls] not in class_dict:
            class_dict[t[cls]] = 1
        else:
            class_dict[t[cls]] += 1
    return max(class_dict.items(), key=operator.itemgetter(1))[0]


k=5
train_data = []
test_data = []
distances = []
data_processing(sys.argv[2], train_data)
data_processing(sys.argv[3], test_data)


guess_set = []
length = len(test_data)
for x in range(length):
    distances.clear()
    for y in range(len(train_data)):
        distances.append((e_distance(test_data[x], train_data[y], 4), train_data[y][4]))
    distances.sort(key=lambda tup: tup[0])
    guess_set.append((get_prediction(distances)[1], test_data[x][4]))

right = 0
total = len(guess_set)
for g in guess_set:
    if g[0] == g[1]:
        right += 1
print("Accuracy: {}".format(right/total))

i = input('Enter vector, data divided by space: ')
i = i.replace(",", ".")
input_vector = i.split()
for num in range(len(input_vector)):
    input_vector[num] = float(input_vector[num])

distances.clear()
for y in range(len(train_data)):
    distances.append((e_distance(input_vector, train_data[y], 4), train_data[y][4]))
distances.sort(key=lambda  tup: tup[0])
print("Guess is: {}".format(get_prediction(distances)[1]))














