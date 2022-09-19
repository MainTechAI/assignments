import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB


data = pd.read_csv('heart.csv')
X = data.drop('target', axis=1).values
y = data.target.values

split_sizes = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
results = []

for size in split_sizes:
    X_train, X_test, y_train, y_test = train_test_split( X, y, 
                                            test_size=size, random_state=42)
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    results.append([
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ])

#%% plot for accuracy

plt.plot(split_sizes, [x[0] for x in results], color='green', lw=2)
plt.xlabel('Test split size (%)')
plt.ylabel('Accuracy')
plt.title('Impact of test split size')
fig = plt.gcf()
fig.set_size_inches(8,6) 
#plt.show()
plt.savefig('accuracy.png')
plt.close()

#%% plot for precision

plt.plot(split_sizes, [x[1] for x in results], color='red', lw=2)
plt.xlabel('Test split size (%)')
plt.ylabel('Precision')
plt.title('Impact of test split size')
fig = plt.gcf()
fig.set_size_inches(8,6) 
#plt.show()
plt.savefig('precision.png')
plt.close()

#%% plot for recall

plt.plot(split_sizes, [x[2] for x in results], color='orange', lw=2)
plt.xlabel('Test split size (%)')
plt.ylabel('Recall')
plt.title('Impact of test split size')
fig = plt.gcf()
fig.set_size_inches(8,6) 
#plt.show()
plt.savefig('recall.png')
plt.close()

#%% f-score

plt.plot(split_sizes, [x[3] for x in results], color='blue', lw=2)
plt.xlabel('Test split size (%)')
plt.ylabel('F-score')
plt.title('Impact of test split size')
fig = plt.gcf()
fig.set_size_inches(8,6) 
#plt.show()
plt.savefig('f-score.png')
plt.close()

