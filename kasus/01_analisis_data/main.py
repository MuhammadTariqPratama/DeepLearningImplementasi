"""Contoh CRISP-DM sederhana: analisis laba, pendapatan, dan piutang sintetis."""
from pathlib import Path
import pandas as pd

OUT = Path(__file__).parent / "output"


def main():
    OUT.mkdir(exist_ok=True)
    # Nilai fiktif dalam juta rupiah; tiap baris adalah satu transaksi.
    transactions = pd.DataFrame([
        ("2025-01-10", "C01", 120, 84), ("2025-02-12", "C02", 90, 59),
        ("2025-03-18", "C01", 110, 79), ("2025-04-03", "C03", 145, 112),
        ("2025-05-20", "C02", 130, 104), ("2025-06-21", "C04", 125, 103),
        ("2025-07-08", "C01", 170, 144), ("2025-08-11", "C05", 160, 138),
        ("2025-09-16", "C03", 155, 133), ("2025-10-02", "C02", 180, 160),
        ("2025-11-14", "C04", 175, 156), ("2025-12-19", "C05", 190, 173),
    ], columns=["date", "customer_id", "revenue_million", "cost_million"])
    transactions["date"] = pd.to_datetime(transactions["date"])
    transactions["quarter"] = transactions.date.dt.to_period("Q").astype(str)
    transactions["profit_million"] = transactions.revenue_million - transactions.cost_million
    quarter = transactions.groupby("quarter", as_index=False).agg(
        revenue_million=("revenue_million", "sum"),
        profit_million=("profit_million", "sum"),
        transactions=("customer_id", "size"),
    )
    quarter["margin_pct"] = (100 * quarter.profit_million / quarter.revenue_million).round(1)

    # Piutang adalah snapshot per invoice, bukan per transaksi penjualan.
    receivables = pd.DataFrame([
        ("INV-01", "C01", 95, 8), ("INV-02", "C02", 140, 41),
        ("INV-03", "C03", 85, 0), ("INV-04", "C04", 210, 73),
        ("INV-05", "C05", 160, 26),
    ], columns=["invoice_id", "customer_id", "amount_million", "days_overdue"])
    receivables["action"] = receivables.days_overdue.map(
        lambda days: "prioritas penagihan" if days >= 30 else "pantau"
    )
    quarter.to_csv(OUT / "ringkasan_kuartal.csv", index=False)
    receivables.sort_values("days_overdue", ascending=False).to_csv(
        OUT / "prioritas_piutang.csv", index=False
    )
    print("Ringkasan kuartal (juta rupiah):")
    print(quarter.to_string(index=False))
    print("\nPiutang yang perlu ditinjau:")
    print(receivables.query("days_overdue >= 30").to_string(index=False))
    print("\nCatatan: data sintetis; gunakan sebagai petunjuk investigasi, bukan kesimpulan sebab.")


if __name__ == "__main__":
    main()
