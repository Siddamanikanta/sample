import pandas as pd
import kagglehub
import matplotlib as plt
import seaborn as sns

print ('hello')

# Download latest version
path = kagglehub.dataset_download("aadarshvelu/heart-failure-prediction-clinical-records")

print("Path to dataset files:", path)

# Load the data
hr_df = pd.read_csv(path + "/heart_failure_clinical_records.csv")

# Print the dataframe
print(hr_df)

# Plot the target feature count
sns.countplot(x=hr_df['DEATH_EVENT'], palette="Set2")
plt.title("Target Distribution (DEATH_EVENT)")
plt.xlabel("Class (0 = Alive, 1 = Death)")
plt.ylabel("Count")
plt.show()