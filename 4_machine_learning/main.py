"""Demo klasifikasi terlambat bayar dengan evaluasi multi-metrik."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, balanced_accuracy_score,
                             classification_report, confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main():
    out = Path(__file__).parent / "output"
    out.mkdir(exist_ok=True)
    rng = np.random.default_rng(17)
    n = 1600
    late_history = rng.poisson(0.45, n)
    invoices = rng.integers(1, 18, n)
    avg_bill = rng.lognormal(2.2, .65, n)
    tenure = rng.integers(1, 72, n)
    logit = -3.0 + .72*late_history + .035*invoices + .0012*avg_bill - .012*tenure
    probability = 1 / (1 + np.exp(-logit))
    y = (rng.random(n) < probability).astype(int)
    X = pd.DataFrame({"late_history": late_history, "invoice_count": invoices,
                      "average_bill": avg_bill, "tenure_months": tenure})
    X.loc[rng.random(n) < .025, "average_bill"] = np.nan
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.25, random_state=42, stratify=y)
    models = {
        "baseline_majority": DummyClassifier(strategy="most_frequent"),
        "logistic_regression": make_pipeline(SimpleImputer(strategy="median"),
                                             StandardScaler(),
                                             LogisticRegression(class_weight="balanced", max_iter=1000)),
    }
    report = {"target_rate": float(y.mean()), "rows": n, "results": {}}
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        report["results"][name] = {
            "accuracy": float(accuracy_score(y_test, pred)),
            "balanced_accuracy": float(balanced_accuracy_score(y_test, pred)),
            "confusion_matrix_labels_0_1": confusion_matrix(y_test, pred, labels=[0, 1]).tolist(),
            "per_class": classification_report(y_test, pred, output_dict=True, zero_division=0),
        }
    (out / "metrik.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Proporsi label terlambat: {report['target_rate']:.1%}")
    for name, result in report["results"].items():
        late = result["per_class"]["1"]
        print(f"{name}: accuracy={result['accuracy']:.3f}, "
              f"recall-terlambat={late['recall']:.3f}, F1-terlambat={late['f1-score']:.3f}")
    print("Metrik lengkap:", out / "metrik.json")


if __name__ == "__main__":
    main()
