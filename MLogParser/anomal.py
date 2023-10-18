import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

#Identifies anomalies in Access Logs


# Assuming 'df' is your DataFrame
df = pd.read_csv('log_data_test.csv')


# Create an encoder object
encoder = LabelEncoder()

# Fit and transform the 'IP' column and replace it in the DataFrame
df['IP'] = encoder.fit_transform(df['IP'])

# Preprocessing: Convert categorical columns to numerical representations
#df['IP'] = df['IP'].apply(lambda x: int(''.join(x.split('.'))))
df['Request'] = df['Request'].astype('category').cat.codes
df['UserAgent'] = df['UserAgent'].astype('category').cat.codes

# Extract features and target
X = df.drop('DateTime', axis=1)

# Fit the model
clf = IsolationForest(contamination=0.01)
clf.fit(X)

# Predict anomalies
pred = clf.predict(X)

# Visualize the results
plt.scatter(X['IP'], X['Request'], c=pred)
plt.xlabel('IP')
plt.ylabel('Request')
plt.title('Anomaly Detection')
plt.show()

# Add the anomaly labels to DataFrame and save it
df['Is_Anomaly'] = pred
df.to_csv('log_with_anomalies.csv', index=False)
