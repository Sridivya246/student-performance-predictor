import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv("student_data.csv")

# Input features
X = data[["study_hours", "attendance", "previous_score", "sleep_hours"]]

# Target
y = data["performance"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)
# Save the trained model
joblib.dump(model, "student_performance_model.pkl")

print("Model saved successfully!")

print("Model trained successfully!")

# Create data for a new student
# Get information from the user
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous score: "))
sleep_hours = float(input("Enter sleep hours: "))

# Create data for the new student
new_student = pd.DataFrame(
    [[study_hours, attendance, previous_score, sleep_hours]],
    columns=["study_hours", "attendance", "previous_score", "sleep_hours"]
)
# Predict performance
prediction = model.predict(new_student)

print("\nPredicted Performance:", prediction[0])

if prediction[0] == "High":
    print("Great! Keep up your good performance.")
elif prediction[0] == "Medium":
    print("Good effort! There is room for improvement.")
else:
    print("Try to improve your study routine and attendance.")

# Check model accuracy
accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)