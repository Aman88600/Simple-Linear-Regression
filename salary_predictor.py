import csv
import matplotlib.pyplot as ptl
data = []
file = open("data_for_salary.csv", newline = "", encoding = "utf-8")
csv_data = csv.reader(file)
for i in csv_data:
    data.append(i)
file.close()

training_data = []
testing_data = []

list_lenght = len(data)
i = 0
while (i < list_lenght):
    if i % 5 == 0:
        testing_data.append(data[i])
    else:
        training_data.append(data[i])
    i += 1
# We have our training_data and testing_data here
sigma_x = 0
sigma_y = 0
sigma_xy = 0
sigma_x2 = 0
n = len(training_data)
print("Training")
for i in training_data:
    sigma_x += float(i[0])
    sigma_y += float(i[1])
    sigma_xy += float(i[0]) * float(i[1])
    sigma_x2 += float(i[0]) * float(i[0])

m = ((n * sigma_xy) - (sigma_x * sigma_y)) / ((n * sigma_x2) - ((sigma_x)*(sigma_x)))
c = (sigma_y - (m * sigma_x)) / n

x_test = []
y_test = []
print("Testing")
for i in testing_data:
    x_test.append(float(i[0]))
    y_test.append(float(i[1]))

x_line = range(0,11)
y_line = [m*xi + c for xi in x_line]

ptl.plot(x_line, y_line, color="blue", label="Prediciton")
ptl.scatter(x_test, y_test, color="red", label="test points")
ptl.legend()
ptl.show()