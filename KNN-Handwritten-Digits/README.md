# KNN - Handwritten Digits (my first ML program)

Classifies handwritten digits (0-9) using K-Nearest Neighbors, on the UCI
"Pen-Based Recognition of Handwritten Digits" dataset (`data/pendigits.*`).

## Run it

```bash
pip install -r requirements.txt
python3 knn_digits.py
```

The script prints an explanation of every step as it runs, and saves three
plots to `outputs/`:

- `samples.png` - what the raw data actually looks like (one drawn digit
  per class, reconstructed from its 8 resampled pen points)
- `k_accuracy.png` - test accuracy for k = 1..15, to show how the choice of
  k affects performance
- `confusion_matrix.png` - which digits the final model confuses most often

See `notes.txt` for a plain-language write-up of what KNN is and what I
learned from this dataset.
