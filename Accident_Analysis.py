import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("US_Accidents_March23.csv")
# Explore the data
print(df.head())
print(df.info())
print(df.describe())

# Analyze patterns related to road conditions
sns.countplot(x='Severity', data=df, hue='Weather_Condition')
plt.title('Traffic Accident Severity by Weather Condition')
plt.show()
# Analyze patterns related to weather
sns.countplot(x='Severity', data=df, hue='Temperature(F)')
plt.title('Traffic Accident Severity by Temperature')
plt.show()
# Analyze patterns related to time of day
df['Hour'] = pd.to_datetime(df['Start_Time']).dt.hour
sns.countplot(x='Hour', data=df, hue='Severity')
plt.title('Traffic Accident Severity by Hour of Day')
plt.show()
# Visualize accident hotspots
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Start_Lng', y='Start_Lat', data=df, hue='Severity', size='Severity')
plt.title('Traffic Accident Hotspots')
plt.show()
# Analyze contributing factors
sns.countplot(x='Severity', data=df, hue='Traffic_Signal')
plt.title('Traffic Accident Severity by Traffic Signal')
plt.show()
# Analyze contributing factors
sns.countplot(x='Severity', data=df, hue='Junction')
plt.title('Traffic Accident Severity by Junction')
plt.show()
# Analyze contributing factors
sns.countplot(x='Severity', data=df, hue='Roundabout')
plt.title('Traffic Accident Severity by Roundabout')
plt.show()

