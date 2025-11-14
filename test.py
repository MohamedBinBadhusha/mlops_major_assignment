from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = fetch_olivetti_faces()
X = data.data
y = data.target

# Train-test split (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Load saved model
model = joblib.load("savedmodel.pth")

# Evaluate accuracy
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"Test Accuracy: {acc * 100:.2f}%")
