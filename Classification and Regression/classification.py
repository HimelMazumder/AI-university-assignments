import numpy as np
from docx import Document

train_set = []
val_set = []
test_set = []

neighbor_set = []
accuracy_set = []

file = 'iris.csv'
dataset = np.genfromtxt(file, delimiter=",").tolist()

np.random.shuffle(dataset)

for S in dataset:
    r = np.random.uniform()

    if 0 <= r <= .7:
        train_set.append(S)
    elif .7 < r <= .85:
        val_set.append(S)
    else:
        test_set.append(S)

K = [1, 3, 5, 10, 15]

for kv in K:
    dst_set = []
    right_prediction = 0

    for SV in val_set:
        x = np.array(SV[0:4])

        for ST in train_set:
            y = np.array(ST[0:4])
            dst = distance = np.linalg.norm(x - y)
            dst_set.append([ST, dst])

        dst_set.sort(key=lambda n: n[1])

        for i in range(kv):
            neighbor_set.append(dst_set[i])

        frequency = {}
        actual_value_set = []

        for j in neighbor_set:
            actual_value_set.append(j[0][4])

        for k in actual_value_set:
            frequency[k] = actual_value_set.count(k)

        pc = max(frequency, key=lambda a: frequency[a])

        if SV[4] == pc:
            right_prediction += 1

        dst_set.clear()
        neighbor_set.clear()

    accuracy = (right_prediction / len(val_set)) * 100
    accuracy_set.append([kv, accuracy])

accuracy_set.sort(key=lambda n: n[1])

doc = Document()

t = doc.add_table(rows=1, cols=2)
t.style = 'Colorful Shading'
row_heading = t.rows[0].cells
row_heading[0].text = 'K'
row_heading[1].text = 'Value Accuracy'

for m in accuracy_set:
    row = t.add_row().cells
    row[0].text = str(m[0])
    row[1].text = str(m[1])

doc.save('classification_table.docx')

print(f"K with highest accuracy is {accuracy_set[0][0]}")

dst_set = []
right_prediction = 0

for SV in test_set:
    x = np.array(SV[0:4])

    for ST in train_set:
        y = np.array(ST[0:4])
        dst = distance = np.linalg.norm(x - y)
        dst_set.append([ST, dst])

    dst_set.sort(key=lambda n: n[1])

    for n in range(accuracy_set[0][0]):
        neighbor_set.append(dst_set[n])

    frequency = {}
    actual_value_set = []

    for p in neighbor_set:
        actual_value_set.append(p[0][4])

    for q in actual_value_set:
        frequency[q] = actual_value_set.count(q)

    pc = max(frequency, key=lambda b: frequency[b])

    if SV[4] == pc:
        right_prediction += 1

    dst_set.clear()
    neighbor_set.clear()

test_accuracy = (right_prediction / len(test_set)) * 100

print(f"Test accuracy is {test_accuracy}")
