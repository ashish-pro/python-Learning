# Statics: Area of mathematics that concerns about data collection, analysis of data.
# Statistics can be used to answer question about the data using some statistical model or ststistical techinqe

# Types of Statistics : 1- Descriptive   2- Infrential
# 1- Descriptive : 1- Measure of central tendency (Mean, Mode, Median)
#                  2- Measure of variability (Range, Variance, Standard Deviation)


# Mode: most frequent value in sample set

#marks = [75, 82,71,92,48,75,97,59,62,75,82,78,66,76,71]
marks = [75, 48,71,92,48,79,97,48,62,70,82,78,48,76,71]
dic = {}
for i in marks:
    if i in dic.keys():
        dic[i] += 1

    else:
        dic[i] = 1
_max = -100
mode = None
for k, v in dic.items():
    if v > _max:
        mode=k
        _max = v
print(mode)