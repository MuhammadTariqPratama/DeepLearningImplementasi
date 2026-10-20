"""Demo memecah skenario komputasi; data dan skor sepenuhnya sintetis."""
import argparse
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import csv


def simulate(task):
    scenario, seed = task
    # Beban mini yang dapat dipecah. Angka ini bukan model lingkungan nyata.
    heat = 30 + (scenario % 12) * 0.8
    vegetation = (scenario * 7 % 100) / 100
    cooling = (scenario * 11 % 60) / 100
    exposure = max(0, heat - 30) * (1 - vegetation) * (1 - cooling)
    return {"scenario": scenario, "seed": seed, "heat_index": round(heat, 2),
            "vegetation_fraction": round(vegetation, 2),
            "cooling_capacity": round(cooling, 2), "exposure_score": round(exposure, 3)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--scenarios", type=int, default=120)
    args = parser.parse_args()
    if args.workers < 1 or args.scenarios < 1:
        parser.error("workers dan scenarios harus >= 1")
    jobs = [(i, 2026) for i in range(args.scenarios)]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(simulate, jobs))
    out = Path(__file__).parent / "output"
    out.mkdir(exist_ok=True)
    with (out / "hasil_skenario.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    top = sorted(results, key=lambda row: row["exposure_score"], reverse=True)[:5]
    print(f"{len(results)} skenario dihitung dengan {args.workers} worker.")
    print("Lima skor paparan tertinggi (contoh sintetis):")
    for row in top:
        print(row)
    print("Output:", out / "hasil_skenario.csv")


if __name__ == "__main__":
    main()
