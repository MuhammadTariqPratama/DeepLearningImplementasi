"""Membuat dashboard HTML mandiri untuk demonstrasi HCI dan visualisasi."""
from pathlib import Path
import json


def main():
    out = Path(__file__).parent / "output"
    out.mkdir(exist_ok=True)
    rows = [
        {"id": "A-101", "month": "Jan", "type": "Pertanian", "region": "Sumatra", "status": "Perlu tinjauan", "count": 18},
        {"id": "A-102", "month": "Feb", "type": "Kebakaran", "region": "Kalimantan", "status": "Ditinjau", "count": 12},
        {"id": "A-103", "month": "Mar", "type": "Penebangan", "region": "Sumatra", "status": "Perlu tinjauan", "count": 21},
        {"id": "A-104", "month": "Apr", "type": "Pertanian", "region": "Papua", "status": "Ditinjau", "count": 16},
        {"id": "A-105", "month": "Mei", "type": "Tambang", "region": "Kalimantan", "status": "Perlu tinjauan", "count": 24},
        {"id": "A-106", "month": "Jun", "type": "Kebakaran", "region": "Papua", "status": "Ditinjau", "count": 14},
    ]
    data = json.dumps(rows, ensure_ascii=False)
    html = """<!doctype html>
<html lang="id"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Alert — Demo</title>
<style>
body{font:16px/1.5 system-ui,sans-serif;margin:0;background:#f4f7f8;color:#18232b}
main{max-width:980px;margin:auto;padding:1.5rem}h1,h2{line-height:1.2}.note{padding:1rem;background:#fff4d6;border-left:5px solid #a76600}
.cards{display:flex;gap:1rem;flex-wrap:wrap}.card,section{background:white;border:1px solid #cbd5da;border-radius:8px;padding:1rem;margin:1rem 0}
.card{min-width:140px;flex:1}.big{font-size:1.7rem;font-weight:700}label{font-weight:600}select{font:inherit;padding:.5rem;margin:.4rem 1rem .4rem .3rem}
table{border-collapse:collapse;width:100%;background:white}th,td{text-align:left;padding:.65rem;border-bottom:1px solid #d8e0e4}th{background:#eaf0f2}
svg{width:100%;height:210px} :focus-visible{outline:3px solid #005fcc;outline-offset:2px}
@media(max-width:600px){main{padding:1rem}table{font-size:.9rem}th,td{padding:.45rem}}
</style>
<main><header><h1>Antrean peringatan lingkungan</h1><p>Ringkasan dan detail untuk membantu petugas memilih alert yang ditinjau.</p></header>
<p class="note"><strong>Demo data sintetis.</strong> Kategori bukan konfirmasi penyebab. Verifikasi lapangan tetap diperlukan.</p>
<section aria-labelledby="overview"><h2 id="overview">Ringkasan periode</h2><div class="cards">
<div class="card"><span>Total alert</span><div class="big" id="total">—</div></div>
<div class="card"><span>Perlu tinjauan</span><div class="big" id="review">—</div></div>
<div class="card"><span>Kategori terlihat</span><div class="big" id="categories">—</div></div></div>
<h2>Tren bulanan</h2><p>Jumlah peringatan pada contoh enam bulan.</p><svg id="trend" role="img" aria-label="Grafik garis jumlah peringatan per bulan"></svg></section>
<section><h2>Filter dan rincian</h2><label for="type">Kategori</label><select id="type"><option value="Semua">Semua kategori</option></select>
<label for="status">Status</label><select id="status"><option value="Semua">Semua status</option><option>Perlu tinjauan</option><option>Ditinjau</option></select>
<div style="overflow-x:auto"><table><thead><tr><th>ID</th><th>Bulan</th><th>Kategori</th><th>Wilayah</th><th>Status</th><th>Jumlah</th></tr></thead><tbody id="rows"></tbody></table></div></section>
<footer><p>Prinsip: ringkasan dahulu, filter berikutnya, detail saat dibutuhkan.</p></footer></main>
<script>
const data=__DATA__,type=document.querySelector('#type'),status=document.querySelector('#status');
[...new Set(data.map(x=>x.type))].forEach(x=>type.add(new Option(x,x)));
function render(){const shown=data.filter(x=>(type.value==='Semua'||x.type===type.value)&&(status.value==='Semua'||x.status===status.value));
document.querySelector('#total').textContent=shown.length;document.querySelector('#review').textContent=shown.filter(x=>x.status==='Perlu tinjauan').length;
document.querySelector('#categories').textContent=new Set(shown.map(x=>x.type)).size;
document.querySelector('#rows').innerHTML=shown.map(x=>`<tr><td>${x.id}</td><td>${x.month}</td><td>${x.type}</td><td>${x.region}</td><td>${x.status}</td><td>${x.count}</td></tr>`).join('');
const svg=document.querySelector('#trend'),w=700,h=190,vals=data.map(x=>x.count),max=Math.max(...vals);
const pts=vals.map((v,i)=>`${30+i*125},${155-v/max*120}`).join(' ');svg.setAttribute('viewBox',`0 0 ${w} ${h}`);
svg.innerHTML=`<line x1="25" y1="155" x2="680" y2="155" stroke="#68777f"/><polyline points="${pts}" fill="none" stroke="#006b63" stroke-width="4"/>`+
data.map((x,i)=>`<circle cx="${30+i*125}" cy="${155-x.count/max*120}" r="5" fill="#006b63"><title>${x.month}: ${x.count} alert</title></circle><text x="${30+i*125}" y="180" text-anchor="middle" font-size="13">${x.month}</text>`).join('');}
type.addEventListener('change',render);status.addEventListener('change',render);render();
</script></html>""".replace("__DATA__", data)
    (out / "dashboard.html").write_text(html, encoding="utf-8")
    print("Dashboard dibuat:", out / "dashboard.html")
    print("Data sintetis; lakukan usability testing dengan pengguna sasaran sebelum digunakan.")


if __name__ == "__main__":
    main()
