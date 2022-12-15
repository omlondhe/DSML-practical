# Compute Accuracy, Error rate, Precision, Recall for the following confusion matrix.

TP = 90
FP = 140
FN = 210
TN = 9560
N = 10000
AP = 300
AN = 9700
PP = 230
PN = 9770

accuracy = (TP + TN) / N
error = 1 - accuracy
precision = TP / PP
recall = TP / AP

print(f"Accuracy: {accuracy}")
print(f"Error rate: {error}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
