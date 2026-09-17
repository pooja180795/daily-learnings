"""
My first machine learning program: classifying handwritten digits with KNN.

Dataset: UCI "Pen-Based Recognition of Handwritten Digits" (pendigits).
Each digit was drawn on a pressure-sensitive tablet, then resampled down to
8 (x, y) points spaced evenly along the pen's path. So every sample is:

    16 numbers (x1, y1, x2, y2, ..., x8, y8), each in the range 0-100
    +
    1 label: the digit that was actually drawn (0-9)

The researchers already split the data into a training file (pendigits.tra)
and a test file (pendigits.tes), written by *different* people, so testing
tells us how well the model generalizes to handwriting it has never seen.

Run this with:  python3 knn_digits.py
It prints an explanation at every step and saves 3 plots into ./outputs/
"""

import os

import numpy as np
import matplotlib
matplotlib.use("Agg")  # write plots to files instead of trying to pop up a window
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
OUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUT_DIR, exist_ok=True)


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------------------------
# STEP 1: Load the data
# ---------------------------------------------------------------------------
section("STEP 1: Load the training and test data")

train_raw = np.loadtxt(os.path.join(DATA_DIR, "pendigits.tra"), delimiter=",")
test_raw = np.loadtxt(os.path.join(DATA_DIR, "pendigits.tes"), delimiter=",")

# Every row is 16 feature columns + 1 label column at the end.
X_train, y_train = train_raw[:, :-1], train_raw[:, -1].astype(int)
X_test, y_test = test_raw[:, :-1], test_raw[:, -1].astype(int)

print(f"Training samples: {X_train.shape[0]}, each with {X_train.shape[1]} features")
print(f"Test samples:     {X_test.shape[0]}, each with {X_test.shape[1]} features")
print("A raw training row looks like this (last value is the true digit):")
print(train_raw[0])


# ---------------------------------------------------------------------------
# STEP 2: Look at the data before doing anything clever
# ---------------------------------------------------------------------------
section("STEP 2: Check how balanced the classes are")

digits, counts = np.unique(y_train, return_counts=True)
for d, c in zip(digits, counts):
    print(f"  digit {d}: {c} training examples")
print("Roughly balanced across 0-9, which is good: KNN can get biased toward")
print("whichever class has the most neighbors lying around.")


# ---------------------------------------------------------------------------
# STEP 3: Visualize a few samples so "16 numbers" becomes a picture of a digit
# ---------------------------------------------------------------------------
section("STEP 3: Draw a few samples as pen trajectories")

fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for digit in range(10):
    ax = axes[digit // 5, digit % 5]
    # first training example for this digit
    sample = X_train[y_train == digit][0]
    xs, ys = sample[0::2], sample[1::2]
    ax.plot(xs, -ys, "-o", markersize=3)  # flip y so the digit isn't upside down
    ax.set_title(str(digit))
    ax.axis("off")
fig.suptitle("One example per digit (8 resampled pen points, connected in order)")
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "samples.png"), dpi=120)
plt.close(fig)
print(f"Saved outputs/samples.png")


# ---------------------------------------------------------------------------
# STEP 4: Feature scaling
# ---------------------------------------------------------------------------
section("STEP 4: Scale the features")

# KNN decides "who is close to me?" using distance between feature vectors,
# so a feature with a bigger numeric range can dominate the distance even if
# it isn't more important. Here every feature is already 0-100, so scaling
# won't change much - but it's a habit worth building for any future dataset
# where features have different units/ranges (e.g. age vs. income).
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # learn mean/std from TRAIN only
X_test_scaled = scaler.transform(X_test)          # apply the same transform to test

print("Before scaling, feature 0 ranges from", X_train[:, 0].min(), "to", X_train[:, 0].max())
print("After scaling,  feature 0 ranges from", round(X_train_scaled[:, 0].min(), 2),
      "to", round(X_train_scaled[:, 0].max(), 2))
print("Note: the scaler is fit on the training data only, then reused on the")
print("test data - fitting it on test data too would leak information from")
print("the test set into training, giving an unrealistically good score.")


# ---------------------------------------------------------------------------
# STEP 5: Train a first KNN model
# ---------------------------------------------------------------------------
section("STEP 5: Train a baseline KNN classifier (k=3)")

# The whole "training" step for KNN is just storing the training data - there
# is no equation to fit. All the work happens later, at prediction time.
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
baseline_acc = accuracy_score(y_test, y_pred)
print(f"k=3 accuracy on the (unseen) test set: {baseline_acc * 100:.2f}%")
print("How a prediction happens: to classify a new digit, KNN measures the")
print("distance from it to every training example, finds the 3 closest ones,")
print("and has them 'vote' on the label by majority.")


# ---------------------------------------------------------------------------
# STEP 6: Try different values of k
# ---------------------------------------------------------------------------
section("STEP 6: Compare different values of k")

# k is the one important knob in KNN:
#   - too small (k=1) -> the model chases noise in the training data (overfitting)
#   - too large        -> the model blurs together digits that are genuinely
#                          different (underfitting)
k_values = list(range(1, 16))
accuracies = []
for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, model.predict(X_test_scaled))
    accuracies.append(acc)
    print(f"  k={k:2d} -> accuracy {acc * 100:.2f}%")

best_k = k_values[int(np.argmax(accuracies))]
best_acc = max(accuracies)
print(f"\nBest k on this test set: k={best_k} with accuracy {best_acc * 100:.2f}%")

plt.figure(figsize=(7, 4))
plt.plot(k_values, [a * 100 for a in accuracies], marker="o")
plt.axvline(best_k, color="grey", linestyle="--", linewidth=1)
plt.xlabel("k (number of neighbors)")
plt.ylabel("Test accuracy (%)")
plt.title("KNN accuracy vs. k")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "k_accuracy.png"), dpi=120)
plt.close()
print("Saved outputs/k_accuracy.png")


# ---------------------------------------------------------------------------
# STEP 7: Final model + confusion matrix
# ---------------------------------------------------------------------------
section(f"STEP 7: Final model with best k={best_k}")

final_model = KNeighborsClassifier(n_neighbors=best_k)
final_model.fit(X_train_scaled, y_train)
y_pred_final = final_model.predict(X_test_scaled)

cm = confusion_matrix(y_test, y_pred_final)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=range(10))
fig, ax = plt.subplots(figsize=(6, 6))
disp.plot(ax=ax, colorbar=False, cmap="Blues")
ax.set_title(f"Confusion matrix (k={best_k})")
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "confusion_matrix.png"), dpi=120)
plt.close(fig)
print("Saved outputs/confusion_matrix.png")
print("\nHow to read the confusion matrix: row = true digit, column = predicted")
print("digit. A perfect model would have a value only on the diagonal.")
print("Whichever off-diagonal cells have the biggest numbers are the digit")
print("pairs KNN confuses most often (commonly digits that are drawn similarly).")

section("Done")
print(f"Final test accuracy with k={best_k}: {accuracy_score(y_test, y_pred_final) * 100:.2f}%")
print("Compare this to the dataset authors' own published k-NN results in")
print("data/pendigits.names (they reported ~97-98% with k between 1 and 11).")
