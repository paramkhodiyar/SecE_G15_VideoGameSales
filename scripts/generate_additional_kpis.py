"""
generate_additional_kpis.py
SecE Group 15 — Video Game Sales Dashboard
Generates 6 additional pre-aggregated CSVs to support new Tableau visualisations.

Output files (all written to data/processed/):
  yoy_growth.csv           — Year, Global_Sales, YoY_Growth_Pct
  platform_timeline.csv    — Platform, First_Year, Last_Year, Lifespan_Years, Total_Sales, Avg_Critic_Score
  developer_kpi.csv        — Developer, Total_Sales, Avg_Critic_Score, Avg_User_Score, Title_Count
  publisher_longevity.csv  — Publisher, Years_Active, Total_Sales, Avg_Critic_Score, Title_Count
  score_gap_by_genre.csv   — Genre, Avg_Score_Gap, Median_Score_Gap, Std_Score_Gap, Critic_Higher_Pct, User_Higher_Pct
  rating_region.csv        — Rating, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales, Title_Count
"""

import csv
import os
from collections import defaultdict
import math

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(BASE, "data", "processed", "video_games_cleaned.csv")
OUT  = os.path.join(BASE, "data", "processed")

# ── Helpers ───────────────────────────────────────────────────────────────────

def flt(v, default=0.0):
    try:
        return float(v)
    except (ValueError, TypeError):
        return default

def mean(lst):
    return sum(lst) / len(lst) if lst else 0.0

def median(lst):
    if not lst:
        return 0.0
    s = sorted(lst)
    n = len(s)
    mid = n // 2
    return (s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2)

def std(lst):
    if len(lst) < 2:
        return 0.0
    m = mean(lst)
    return math.sqrt(sum((x - m) ** 2 for x in lst) / len(lst))

def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  ✓  Written: {os.path.relpath(path, BASE)}")

# ── Load data ─────────────────────────────────────────────────────────────────
print("Loading video_games_cleaned.csv …")
with open(SRC, encoding="utf-8") as f:
    data = list(csv.DictReader(f))
print(f"  Rows loaded: {len(data)}\n")

# ═══════════════════════════════════════════════════════════════════════════════
# 1. YoY Growth
# ═══════════════════════════════════════════════════════════════════════════════
print("1. Generating yoy_growth.csv …")
year_sales = defaultdict(float)
for r in data:
    yr = r["Year_of_Release"].strip()
    if yr.isdigit():
        year_sales[int(yr)] += flt(r["Global_Sales"])

years_sorted = sorted(year_sales.keys())
rows_yoy = []
for i, yr in enumerate(years_sorted):
    sales = year_sales[yr]
    if i == 0:
        growth = None
    else:
        prev = year_sales[years_sorted[i - 1]]
        growth = round((sales - prev) / abs(prev) * 100, 2) if prev else None
    rows_yoy.append({
        "Year_of_Release": yr,
        "Global_Sales":    round(sales, 2),
        "YoY_Growth_Pct":  growth if growth is not None else "",
    })

write_csv(
    os.path.join(OUT, "yoy_growth.csv"),
    ["Year_of_Release", "Global_Sales", "YoY_Growth_Pct"],
    rows_yoy,
)

# ═══════════════════════════════════════════════════════════════════════════════
# 2. Platform Timeline
# ═══════════════════════════════════════════════════════════════════════════════
print("2. Generating platform_timeline.csv …")
plat = defaultdict(lambda: {
    "years": [], "sales": 0.0, "scores": []
})
for r in data:
    p = r["Platform"].strip()
    yr = r["Year_of_Release"].strip()
    if yr.isdigit():
        plat[p]["years"].append(int(yr))
    plat[p]["sales"] += flt(r["Global_Sales"])
    cs = flt(r["Critic_Score"], None)
    if cs is not None and cs > 0:
        plat[p]["scores"].append(cs)

rows_pt = []
for p, d in plat.items():
    if not d["years"]:
        continue
    first = min(d["years"])
    last  = max(d["years"])
    rows_pt.append({
        "Platform":        p,
        "First_Year":      first,
        "Last_Year":       last,
        "Lifespan_Years":  last - first,
        "Total_Sales":     round(d["sales"], 2),
        "Avg_Critic_Score": round(mean(d["scores"]), 2) if d["scores"] else "",
    })

rows_pt.sort(key=lambda x: -x["Total_Sales"])
write_csv(
    os.path.join(OUT, "platform_timeline.csv"),
    ["Platform", "First_Year", "Last_Year", "Lifespan_Years", "Total_Sales", "Avg_Critic_Score"],
    rows_pt,
)

# ═══════════════════════════════════════════════════════════════════════════════
# 3. Developer KPI
# ═══════════════════════════════════════════════════════════════════════════════
print("3. Generating developer_kpi.csv …")
devs = defaultdict(lambda: {
    "sales": 0.0, "scores": [], "user_scores": [], "titles": set()
})
for r in data:
    d = r["Developer"].strip()
    if not d or d.lower() in ("unknown", ""):
        continue
    devs[d]["sales"] += flt(r["Global_Sales"])
    cs = flt(r["Critic_Score"], None)
    if cs and cs > 0:
        devs[d]["scores"].append(cs)
    us = flt(r["User_Score"], None)
    if us and us > 0:
        devs[d]["user_scores"].append(us)
    devs[d]["titles"].add(r["Name"].strip())

rows_dev = []
for d, v in devs.items():
    rows_dev.append({
        "Developer":       d,
        "Total_Sales":     round(v["sales"], 2),
        "Avg_Critic_Score": round(mean(v["scores"]), 2) if v["scores"] else "",
        "Avg_User_Score":  round(mean(v["user_scores"]), 2) if v["user_scores"] else "",
        "Title_Count":     len(v["titles"]),
    })

rows_dev.sort(key=lambda x: -x["Total_Sales"])
write_csv(
    os.path.join(OUT, "developer_kpi.csv"),
    ["Developer", "Total_Sales", "Avg_Critic_Score", "Avg_User_Score", "Title_Count"],
    rows_dev,
)

# ═══════════════════════════════════════════════════════════════════════════════
# 4. Publisher Longevity
# ═══════════════════════════════════════════════════════════════════════════════
print("4. Generating publisher_longevity.csv …")
pubs = defaultdict(lambda: {
    "years": [], "sales": 0.0, "scores": [], "titles": set()
})
for r in data:
    p = r["Publisher"].strip()
    yr = r["Year_of_Release"].strip()
    if yr.isdigit():
        pubs[p]["years"].append(int(yr))
    pubs[p]["sales"] += flt(r["Global_Sales"])
    cs = flt(r["Critic_Score"], None)
    if cs and cs > 0:
        pubs[p]["scores"].append(cs)
    pubs[p]["titles"].add(r["Name"].strip())

rows_pub = []
for p, v in pubs.items():
    if not v["years"]:
        continue
    years_active = max(v["years"]) - min(v["years"])
    rows_pub.append({
        "Publisher":       p,
        "Years_Active":    years_active,
        "First_Year":      min(v["years"]),
        "Last_Year":       max(v["years"]),
        "Total_Sales":     round(v["sales"], 2),
        "Avg_Critic_Score": round(mean(v["scores"]), 2) if v["scores"] else "",
        "Title_Count":     len(v["titles"]),
    })

rows_pub.sort(key=lambda x: -x["Total_Sales"])
write_csv(
    os.path.join(OUT, "publisher_longevity.csv"),
    ["Publisher", "Years_Active", "First_Year", "Last_Year",
     "Total_Sales", "Avg_Critic_Score", "Title_Count"],
    rows_pub,
)

# ═══════════════════════════════════════════════════════════════════════════════
# 5. Score Gap by Genre
# ═══════════════════════════════════════════════════════════════════════════════
print("5. Generating score_gap_by_genre.csv …")
genre_gaps = defaultdict(list)
for r in data:
    g = r["Genre"].strip()
    sg = flt(r["Score_Gap"], None)
    if sg is not None:
        genre_gaps[g].append(sg)

rows_sg = []
for g, gaps in genre_gaps.items():
    critic_higher = sum(1 for x in gaps if x < 0)   # Score_Gap < 0 → Critic < User*10 → Users rate higher
    user_higher   = sum(1 for x in gaps if x > 0)
    rows_sg.append({
        "Genre":              g,
        "Game_Count":         len(gaps),
        "Avg_Score_Gap":      round(mean(gaps), 3),
        "Median_Score_Gap":   round(median(gaps), 3),
        "Std_Score_Gap":      round(std(gaps), 3),
        "Critic_Higher_Pct":  round(user_higher / len(gaps) * 100, 1),   # positive gap = critic higher
        "User_Higher_Pct":    round(critic_higher / len(gaps) * 100, 1), # negative gap = user higher
    })

rows_sg.sort(key=lambda x: x["Avg_Score_Gap"])
write_csv(
    os.path.join(OUT, "score_gap_by_genre.csv"),
    ["Genre", "Game_Count", "Avg_Score_Gap", "Median_Score_Gap", "Std_Score_Gap",
     "Critic_Higher_Pct", "User_Higher_Pct"],
    rows_sg,
)

# ═══════════════════════════════════════════════════════════════════════════════
# 6. Rating × Region Breakdown
# ═══════════════════════════════════════════════════════════════════════════════
print("6. Generating rating_region.csv …")
ratings_data = defaultdict(lambda: {
    "na": 0.0, "eu": 0.0, "jp": 0.0, "other": 0.0, "global": 0.0, "count": 0
})
for r in data:
    rt = r["Rating"].strip()
    if not rt or rt.lower() in ("unknown", ""):
        rt = "Unknown"
    ratings_data[rt]["na"]     += flt(r["NA_Sales"])
    ratings_data[rt]["eu"]     += flt(r["EU_Sales"])
    ratings_data[rt]["jp"]     += flt(r["JP_Sales"])
    ratings_data[rt]["other"]  += flt(r["Other_Sales"])
    ratings_data[rt]["global"] += flt(r["Global_Sales"])
    ratings_data[rt]["count"]  += 1

rows_rt = []
for rt, v in ratings_data.items():
    rows_rt.append({
        "Rating":       rt,
        "NA_Sales":     round(v["na"], 2),
        "EU_Sales":     round(v["eu"], 2),
        "JP_Sales":     round(v["jp"], 2),
        "Other_Sales":  round(v["other"], 2),
        "Global_Sales": round(v["global"], 2),
        "Title_Count":  v["count"],
    })

rows_rt.sort(key=lambda x: -x["Global_Sales"])
write_csv(
    os.path.join(OUT, "rating_region.csv"),
    ["Rating", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales", "Title_Count"],
    rows_rt,
)

print("\n✅  All 6 KPI files generated successfully in data/processed/")
