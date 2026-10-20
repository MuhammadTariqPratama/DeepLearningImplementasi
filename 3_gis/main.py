"""Saringan lokasi gerai dengan fitur geospasial sintetis; tanpa GIS eksternal."""
from pathlib import Path
import csv
import json
from math import asin, cos, radians, sin, sqrt

OUT = Path(__file__).parent / "output"


def distance_km(a, b):
    """Jarak lingkaran besar antara (lat, lon), dalam kilometer."""
    lat1, lon1 = a
    lat2, lon2 = b
    dlat, dlon = radians(lat2-lat1), radians(lon2-lon1)
    h = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    return 6371 * 2 * asin(sqrt(h))


def main():
    OUT.mkdir(exist_ok=True)
    candidates = [
        {"id": "A", "name": "Utara", "lat": -6.18, "lon": 106.82, "population": 8500, "road_km": .2, "competitor_km": 2.4, "transit_km": .5},
        {"id": "B", "name": "Barat", "lat": -6.21, "lon": 106.78, "population": 6200, "road_km": .1, "competitor_km": .7, "transit_km": .3},
        {"id": "C", "name": "Timur", "lat": -6.20, "lon": 106.87, "population": 11000, "road_km": .8, "competitor_km": 3.1, "transit_km": 1.1},
        {"id": "D", "name": "Selatan", "lat": -6.25, "lon": 106.84, "population": 7300, "road_km": .3, "competitor_km": 1.8, "transit_km": .4},
    ]
    hub = (-6.20, 106.82)
    for row in candidates:
        row["distance_hub_km"] = round(distance_km(hub, (row["lat"], row["lon"])), 2)
        # Aturan skor demonstrasi, bukan model yang divalidasi.
        row["score"] = round(
            row["population"] / 1000 + 2/(row["road_km"] + 1)
            + min(row["competitor_km"], 4) * .6 - row["transit_km"] * .5, 2)
    ranked = sorted(candidates, key=lambda row: row["score"], reverse=True)
    with (OUT / "peringkat_kandidat.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ranked[0].keys())
        writer.writeheader(); writer.writerows(ranked)
    features = [{"type": "Feature", "properties": row,
                 "geometry": {"type": "Point", "coordinates": [row["lon"], row["lat"]]}}
                for row in ranked]
    (OUT / "kandidat.geojson").write_text(
        json.dumps({"type": "FeatureCollection", "features": features}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print("Urutan kandidat (sintetis):")
    for rank, row in enumerate(ranked, 1):
        print(f"{rank}. {row['name']} — skor {row['score']}")
    print("Berkas GeoJSON dapat dibuka di QGIS:", OUT / "kandidat.geojson")


if __name__ == "__main__":
    main()
