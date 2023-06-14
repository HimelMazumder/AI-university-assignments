import numpy as np
from docx import Document

train_set = []
val_set = []
test_set = []

neighbor_set = []
mean_square_error_set = []

file = 'diabetes.csv'
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
    error = 0

    for SV in val_set:
        x = np.array(SV[0:4])

        for ST in train_set:
            y = np.array(ST[0:4])
            dst = distance = np.linalg.norm(x - y)
            dst_set.append([ST, dst])

        dst_set.sort(key=lambda n: n[1])

        for i in range(kv):
            neighbor_set.append(dst_set[i])

        total = 0
        for j in neighbor_set:
            total = total + j[0][4]

        pv = total / len(neighbor_set)
        error = error + ((SV[4] - pv) ** 2)

        dst_set.clear()
        neighbor_set.clear()

    mean_square_error = error / len(val_set)
    mean_square_error_set.append([kv, mean_square_error])

mean_square_error_set.sort(key=lambda n: n[1])

doc = Document()

t = doc.add_table(rows=1, cols=2)
t.style = 'Colorful Shading'
row_heading = t.rows[0].cells
row_heading[0].text = 'K'
row_heading[1].text = 'Mean Square Error'

for k in mean_square_error_set:
    row = t.add_row().cells
    row[0].text = str(k[0])
    row[1].text = str(k[1])

doc.save('regression_table.docx')

print(f"K with least mean square error is {mean_square_error_set[0][0]}")

dst_set = []
error = 0

for SV in test_set:
    x = np.array(SV[0:4])

    for ST in train_set:
        y = np.array(ST[0:4])
        dst = distance = np.linalg.norm(x - y)
        dst_set.append([ST, dst])

    dst_set.sort(key=lambda n: n[1])

    for i in range(mean_square_error_set[0][0]):
        neighbor_set.append(dst_set[i])

    total = 0
    for j in neighbor_set:
        total = total + j[0][4]

    pv = total / len(neighbor_set)
    error = error + ((SV[4] - pv) ** 2)

    dst_set.clear()
    neighbor_set.clear()

test_mean_square_error = error / len(val_set)

print(f"Test mean square error is {test_mean_square_error}")
