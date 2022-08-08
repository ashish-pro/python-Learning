# Statics: Area of mathematics that concerns about data collection, analysis of data.
# Statistics can be used to answer question about the data using some statistical model or ststistical techinqe

# Types of Statistics : 1- Descriptive   2- Infrential
# 1- Descriptive : 1- Measure of central tendency (Mean, Mode, Median)
#                  2- Measure of variability (Range, Variance, Standard Deviation)


# Mode: It is a central value of sample set in ordered way

marks = [2,4,6,8]
sorted_marks = sorted(marks)
len_list = len(sorted_marks)
if len_list % 2 ==0:
    index_1 = len(sorted_marks)//2
    index_2 = index_1 - 1
    median = (sorted_marks[index_1]+sorted_marks[index_2])//2
    print(median)
else:
    index = len(sorted_marks)//2
    median = sorted_marks[index]
    print(median)
