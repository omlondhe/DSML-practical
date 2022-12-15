# Compute Accuracy, Error rate, Precision, Recall for following confusion matrix (Use formula for each)

TP = 1
FP = 1
FN = 8
TN = 90

accuracy = (TP + TN) / (TP + TN + FP + FN)
error = 1 - accuracy
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print(f"Accuracy: {accuracy}")
print(f"Error rate: {error}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
