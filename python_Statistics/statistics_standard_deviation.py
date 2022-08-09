# Standard deviation : spread of data from mean value

marks = [75, 82,71,92,48,75,97,59,62,75,82,78,66,76,71]
mean_marks = sum(marks)/len(marks)
print(mean_marks)
sum = 0
for i in range(len(marks)):
    sum = (marks[i]-round(mean_marks))**2
var = sum/len(marks)
print(var)

standaerd_deviation = var ** 0.5
print(standaerd_deviation)