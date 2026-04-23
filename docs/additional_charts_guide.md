# 🎮 Additional Charts Guide — SecE Group 15
## Step-by-Step Instructions for 6 New Visualisations

> **Author**: Aaditya Yadav  
> **Builds on top of**: `tableau_dashboard_guide.md`  
> **New data files** (already generated in `data/processed/`):
> - `yoy_growth.csv`
> - `platform_timeline.csv`
> - `developer_kpi.csv`
> - `publisher_longevity.csv`
> - `score_gap_by_genre.csv`
> - `rating_region.csv`

---

## Step 0 — Connect the 6 New Data Sources

Before building any new chart, connect all 6 new CSVs to your Tableau workbook.

1. From the top menu: **Data → New Data Source → Text file**.
2. Navigate to `SecE_G15_VideoGameSales/data/processed/`.
3. Open `yoy_growth.csv` → click **Open**.
4. Repeat for each of the remaining 5 files:
   - `platform_timeline.csv`
   - `developer_kpi.csv`
   - `publisher_longevity.csv`
   - `score_gap_by_genre.csv`
   - `rating_region.csv`
5. You now have **10 data sources** in the Data pane. Switch between them using the dropdown at the top of the Data pane.

---

## Chart N1 — Year-over-Year Sales Growth (Dual-Axis: Bar + Line)
### → Adds to: **Page 1 — Executive Overview**

> **What it shows**: Raw annual sales as bars (left axis) + YoY % change as a line (right axis).  
> **Key insight**: The industry grew 35% YoY in 2007 — its largest single-year spike — then declined from 2009 onward.  
> **Data source**: `yoy_growth.csv`

### Build the chart

1. **New Worksheet** → rename to `YoY Growth`.
2. In the Data pane dropdown, switch to **yoy_growth.csv**.
3. Check column types:
   - `Year_of_Release` → change to **Number (Whole)** if it shows as Abc.
   - `YoY_Growth_Pct` → should be **Number (decimal)**.
4. **Drag** `Year_of_Release` → **Columns** shelf. Right-click the pill → **Dimension** (so each year is a discrete point, not aggregated).
5. **Drag** `Global_Sales` → **Rows** shelf (SUM).
6. **Drag** `Yoy_Growth_Pct` → **Rows** shelf — **next to** (not on top of) the existing `SUM(Global_Sales)` pill.
   - You now have two rows measures and two separate charts stacked.
7. Right-click the `SUM(Global_Sales)` pill on Rows → **Dual Axis**.
   - The chart now shares one X-axis with two Y-axes.
8. Right-click the right Y-axis → **Synchronize Axis** — **do NOT click this** (the axes should stay independent because they measure different things).
9. In the Marks card, you will see two sub-cards: one for `Global_Sales`, one for `Yoy_Growth_Pct`.
   - Click the **`Global_Sales`** sub-card → change type to **Bar** → set Color to `#3A86FF` (steel blue).
   - Click the **`Yoy_Growth_Pct`** sub-card → change type to **Line** → set Color to `#FF6B35` (orange).
10. For the growth line, click the **`Yoy_Growth_Pct`** sub-card → click **Label** → check **Show mark labels** → under **Marks to label**, select **Min/Max** (shows only peak and trough labels to avoid clutter).
11. Add a zero reference line on the right axis:
    - Right-click the **right Y-axis** → **Add Reference Line**.
    - **Scope**: Entire Table. **Value**: Constant → type `0`. **Label**: Custom → `"No Growth"`. **Line**: Dashed, gray.
    - Click **OK**.
12. Format axes:
    - Right-click left Y-axis → **Edit Axis** → Title: `Global Sales ($M)`.
    - Right-click right Y-axis → **Edit Axis** → Title: `YoY Growth (%)`.
    - Right-click X-axis → **Edit Axis** → Title: `Year`.
13. Add an annotation at the 2007 peak:
    - Right-click the bar for 2007 → **Annotate → Mark** → type `"Peak: $704M (+35%)"` → click **OK**.

### Add to Dashboard

1. Open the **Executive Overview** dashboard.
2. The existing `Sales Trend` chart shows cumulative sales over time. Place `YoY Growth` **below** it.
3. Drag a new **Horizontal** container below the Sales Trend area.
4. Drag `YoY Growth` into that container — span full width, ~200px height.
5. Right-click its title → **Edit Title** → `Year-over-Year Sales Growth`.

---

## Chart N2 — Platform Lifecycle Timeline (Gantt Chart)
### → Adds to: **Page 1 — Executive Overview**

> **What it shows**: Each platform as a horizontal bar running from its first to last active year, coloured by total sales.  
> **Key insight**: PS2 had the longest commercial lifespan of any high-sales platform (11 years, 2000–2011). Some platforms like GBA lasted even longer but at far lower revenue.  
> **Data source**: `platform_timeline.csv`

### Build the chart

1. **New Worksheet** → rename to `Platform Timeline`.
2. In the Data pane dropdown, switch to **platform_timeline.csv**.
3. Check column types:
   - `First_Year`, `Last_Year`, `Lifespan_Years` → **Number (Whole)**.
   - `Total_Sales`, `Avg_Critic_Score` → **Number (decimal)**.
4. **Drag** `First_Year` → **Columns** shelf. Right-click the pill → **Dimension**.
5. **Drag** `Platform` → **Rows** shelf.
6. In the Marks card dropdown → change to **Gantt Bar**.
7. **Drag** `Lifespan_Years` → **Size** on the Marks card. The bar now spans from `First_Year` for `Lifespan_Years` years.
8. Filter to Top 20 platforms by sales:
   - **Drag** `Total_Sales` → **Filters** card.
   - In the filter dialog → **At least** → type `100` → **OK**. *(This keeps platforms with ≥ 100M sales.)*
   - Alternatively: right-click `Platform` → **Sort → Descending → Field: Total_Sales → Sum** and manually hide the smallest ones.
9. Sort rows so biggest-selling platforms are at the top:
   - Right-click `Platform` on the Rows shelf → **Sort → Descending → Field: Total_Sales → Sum**.
10. **Drag** `Total_Sales` → **Color** on the Marks card.
    - Click **Color → Edit Colors** → choose a sequential palette (e.g., **Blue**). Highest sales = darkest.
    - Click **OK**.
11. **Drag** `Avg_Critic_Score` → **Tooltip** on the Marks card.
12. Click **Label** in Marks card → check **Show mark labels** → drag `Lifespan_Years` into the label → format as `<Lifespan_Years> yrs`.
13. Format the X-axis:
    - Right-click X-axis → **Edit Axis** → Title: `Year`. Set **Fixed range**: Start `1980`, End `2016`.

### Add to Dashboard

1. On the **Executive Overview** dashboard, drag `Platform Timeline` below the `YoY Growth` chart.
2. Full width, ~200px height.
3. Edit title → `Console Lifespan & Revenue (Top Platforms)`.

---

## Chart N3 — Top 10 Developers by Global Sales (Horizontal Bar)
### → Adds to: **Page 2 — Genre & Platform Deep Dive**

> **What it shows**: The top 10 game-developing studios ranked by total sales, with bars coloured by their average Critic Score.  
> **Key insight**: Rockstar North produced only 5 titles but ranked in the top 5 by revenue (~$120M), making it the highest revenue-per-title studio. Nintendo dominates with $530M across 71 titles.  
> **Data source**: `developer_kpi.csv`

### Build the chart

1. **New Worksheet** → rename to `Developer Sales`.
2. In the Data pane dropdown, switch to **developer_kpi.csv**.
3. Check column types:
   - `Total_Sales`, `Avg_Critic_Score`, `Avg_User_Score` → **Number (decimal)**.
   - `Title_Count` → **Number (Whole)**.
4. **Drag** `Developer` → **Rows** shelf.
5. **Drag** `Total_Sales` → **Columns** shelf (SUM — but since this is pre-aggregated, each developer has one row, so SUM = the value).
6. Filter to Top 10:
   - **Drag** `Total_Sales` → **Filters** card → **At least** → type `100` → **OK**.  
   *(This keeps only developers with ≥ 100M sales, which gives exactly the top 10.)*
7. Sort descending: click the **Sort Descending** icon in the toolbar (bar chart icon with down-arrow).
8. **Drag** `Avg_Critic_Score` → **Color** on the Marks card.
   - Click **Color → Edit Colors** → choose **Green-Gold** sequential palette. Higher score = darker green.
   - Click **OK**.
9. **Drag** `Title_Count` → **Label** on the Marks card. Click **Label** → check **Show mark labels**. Edit the label text to show both sales and titles:
   - Click the `...` button next to the label → in the editor, type: `<Total_Sales>M  (<Title_Count> titles)`.
10. Add an average reference line:
    - Right-click X-axis → **Add Reference Line** → **Scope**: Entire Table → **Value**: Average of `Total_Sales` → **Label**: Custom → `"Top 10 Avg"` → Dashed gray.
    - Click **OK**.
11. Format:
    - Right-click X-axis → **Edit Axis** → Title: `Total Global Sales ($M)`.

### Add to Dashboard

1. Open the **Genre & Platform Deep Dive** dashboard.
2. Drag a new **Horizontal** container below the existing bottom row (below Genre Critic Scores and Genre by Era).
3. Drag `Developer Sales` into the **left half** of that container (~50% width).
4. Edit title → `Top 10 Developers by Revenue (Colour = Critic Score)`.

---

## Chart N4 — Publisher Longevity vs Revenue (Scatter Plot)
### → Adds to: **Page 2 — Genre & Platform Deep Dive** (right of Developer Sales)

> **What it shows**: Each publisher plotted as a circle — X = years active, Y = total global sales, bubble size = number of titles.  
> **Key insight**: Activision has been active the longest (36 years) but Nintendo generates more revenue despite similar longevity. Short-lived high-revenue publishers are "one-hit wonders".  
> **Data source**: `publisher_longevity.csv`

### Build the chart

1. **New Worksheet** → rename to `Publisher Longevity`.
2. In the Data pane dropdown, switch to **publisher_longevity.csv**.
3. Check column types:
   - `Years_Active`, `First_Year`, `Last_Year`, `Title_Count` → **Number (Whole)**.
   - `Total_Sales`, `Avg_Critic_Score` → **Number (decimal)**.
4. **Drag** `Years_Active` → **Columns** shelf (SUM — pre-aggregated, so SUM = value).
5. **Drag** `Total_Sales` → **Rows** shelf (SUM).
6. **Drag** `Publisher` → **Detail** on the Marks card (creates one mark per publisher).
7. Filter to Top 30 publishers:
   - **Drag** `Total_Sales` → **Filters** → **At least** → type `30` → **OK**.
8. **Drag** `Title_Count` → **Size** on the Marks card. Click **Size** → slide to the right to increase bubble sizes.
9. **Drag** `Avg_Critic_Score` → **Color** on Marks card (sequential palette). Higher score = darker color.
10. Marks card dropdown → **Circle**. Click **Color** → set **Opacity** to 75%.
11. **Drag** `Publisher` → **Label** on Marks card. Click **Label** → under **Marks to label**, select **Min/Max** → check **Max** only (labels only the highest-sales publisher per side).
    - To manually label key publishers: right-click a specific dot → **Mark Label → Always Show**.
12. Add a linear trend line:
    - Go to **Analysis menu → Trend Lines → Show Trend Lines**.
13. Customize the tooltip:
    - Click **Tooltip** in Marks → **Edit Tooltip** → add: `Publisher: <Publisher>`, `Years Active: <Years_Active>`, `Total Sales: <Total_Sales>M`, `Titles: <Title_Count>`, `Avg Critic Score: <Avg_Critic_Score>`.
14. Format axes:
    - X-axis title: `Years Publisher Was Active`.
    - Y-axis title: `Total Global Sales ($M)`.

### Add to Dashboard

1. In the **Genre & Platform Deep Dive** dashboard, drag `Publisher Longevity` into the **right half** of the same new container as Developer Sales (~50% width).
2. Edit title → `Publisher Longevity vs Revenue (Size = Titles, Colour = Critic Score)`.

---

## Chart N5 — Score Gap by Genre (Bar Chart with Diverging Color)
### → Adds to: **Page 3 — Regional & Ratings Analysis**

> **What it shows**: Average Score Gap per genre (positive = critics rated higher; negative = users rated higher). Sorted from most user-favoured to most critic-favoured.  
> **Key insight**: Sports and Shooter games have the smallest gap (users and critics roughly agree). Platform, Puzzle, and Adventure games are rated much higher by users than by critics.  
> **Data source**: `score_gap_by_genre.csv`

### Build the chart

1. **New Worksheet** → rename to `Score Gap by Genre`.
2. In the Data pane dropdown, switch to **score_gap_by_genre.csv**.
3. Check column types:
   - `Game_Count` → **Number (Whole)**.
   - `Avg_Score_Gap`, `Median_Score_Gap`, `Std_Score_Gap`, `Critic_Higher_Pct`, `User_Higher_Pct` → **Number (decimal)**.
4. **Drag** `Genre` → **Rows** shelf.
5. **Drag** `Avg_Score_Gap` → **Columns** shelf (SUM — pre-aggregated).
6. Sort ascending so most user-favoured genres (most negative gap) appear at the top:
   - Right-click `Genre` on Rows → **Sort → Ascending → Field: Avg_Score_Gap → Sum**.
7. **Drag** `Avg_Score_Gap` → **Color** on Marks card.
   - Click **Color → Edit Colors** → choose **Red-Blue Diverging** palette.
   - Check **Use Full Color Range**. Set **Center** to `0`.
   - Negative (blue) = users rate higher. Positive (red) = critics rate higher.
   - Click **OK**.
8. Add data labels:
   - Click **Label** in Marks → check **Show mark labels**.
   - Format the label to 1 decimal place.
9. Add a reference line at 0:
   - Right-click the X-axis → **Add Reference Line** → Constant → `0` → Label: Custom → `"Parity"` → Solid black, line weight 2.
   - Click **OK**.
10. Add annotations:
    - Right-click the right side of the chart (positive X area) → **Annotate → Area** → type `"Critics rate higher"` → click **OK**.
    - Right-click the left side → **Annotate → Area** → type `"Users rate higher"` → click **OK**.
11. **Drag** `Game_Count` and `User_Higher_Pct` → **Tooltip** on Marks card.
12. Format:
    - X-axis title: `Average Score Gap  (Critic Score − User Score × 10)`.

### Add to Dashboard

1. Open the **Regional & Ratings Analysis** dashboard.
2. Drag `Score Gap by Genre` below the existing `Score Gap` histogram.
3. Full width, ~220px height.
4. Edit title → `Average Score Gap by Genre — Who Rates Higher?`.

---

## Chart N6 — ESRB Rating × Regional Sales Breakdown (100% Stacked Bar)
### → Adds to: **Page 3 — Regional & Ratings Analysis**

> **What it shows**: For each ESRB content rating (E, T, M, E10+, etc.), how the total sales split across NA, EU, JP, and Other — shown as 100% proportions.  
> **Key insight**: M-rated (Mature) games derive only 4.4% of their sales from Japan vs 50.8% from NA — a stark contrast to E-rated games which are much more balanced across regions.  
> **Data source**: `rating_region.csv`

### Build the chart

1. **New Worksheet** → rename to `Rating by Region`.
2. In the Data pane dropdown, switch to **rating_region.csv**.
3. Check column types:
   - `Title_Count` → **Number (Whole)**.
   - `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales` → **Number (decimal)**.
4. Filter out low-value ratings first:
   - **Drag** `Rating` → **Filters** card.
   - In the dialog, go to the **General** tab → check only: `E`, `T`, `M`, `E10+`, `Unknown`.
   - Uncheck `AO`, `EC`, `K-A`, `RP` (these have < 10 titles total and will clutter the chart).
   - Click **OK**.
5. **Drag** `Rating` → **Rows** shelf.
6. In the Marks card, use **Measure Names / Measure Values** for the 4 region columns:
   - Double-click `Measure Names` in the Data pane — it appears on the Marks card automatically.
   - **Drag** `Measure Names` → **Color** on the Marks card.
   - **Drag** `Measure Values` → **Columns** shelf.
7. A Measure Names filter appears on the Filters card. Click it:
   - Uncheck all → check only `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`.
   - Click **OK**.
8. Marks card dropdown → **Bar**.
9. Make it 100% stacked:
   - Click the `SUM(Measure Values)` pill on Columns → **Quick Table Calculation → Percent of Total**.
   - Right-click the pill → **Edit Table Calculation** → **Compute Using → Measure Names**.
10. Sort rows by total Global_Sales (largest rating first):
    - Right-click `Rating` on Rows → **Sort → Descending → Field: Global_Sales → Sum**.
11. Set region colors (match the rest of the dashboard):
    - Click **Color → Edit Colors**:
      - `NA_Sales` → `#3A86FF` (blue).
      - `EU_Sales` → `#06D6A0` (teal/green).
      - `JP_Sales` → `#EF476F` (red/pink).
      - `Other_Sales` → `#FFD166` (amber).
    - Click **OK**.
12. Add percentage labels:
    - Click **Label** → check **Show mark labels**.
    - In the label editor → format to **1 decimal place**, show `%`.
13. **Drag** `Title_Count` → **Tooltip** on Marks.
14. Format:
    - Right-click X-axis → **Edit Axis** → Title: `Share of Regional Sales (%)`. Fixed range: 0 to 100.
    - Right-click Y-axis → **Edit Axis** → Title: `ESRB Rating`.

### Add to Dashboard

1. On the **Regional & Ratings Analysis** dashboard, add `Rating by Region` as a **full-width** row at the very bottom.
2. Height ~200px.
3. Edit title → `Regional Sales Split by ESRB Rating (% of Total)`.

---

## Final Dashboard Layouts After All Additions

### Page 1 — Executive Overview

```
┌────────────────────────────────────────────────────────┐
│  Title + Filters (Era / Genre / Platform)              │
├──────────┬──────────┬──────────┬──────────────────────┤
│ KPI:$    │ KPI:#    │ KPI:Crit │ KPI:User             │
├──────────┴──────────┴──────────┴──────────────────────┤
│  [existing] Sales Trend (Line Chart)                   │
├────────────────────────────────────────────────────────┤
│  [N1] YoY Growth % (Dual-Axis Bar + Line)  ← NEW     │
├────────────────────────────────────────────────────────┤
│  [N2] Platform Lifecycle Gantt             ← NEW     │
├───────────────────────┬────────────────────────────────┤
│  Top 10 Games (Bar)   │  Regional Sales (Pie)          │
│  [existing]           │  [existing]                   │
└───────────────────────┴────────────────────────────────┘
```

### Page 2 — Genre & Platform Deep Dive

```
┌────────────────────────────────────────────────────────┐
│  Title + Filters                                       │
├───────────────────────┬────────────────────────────────┤
│  Genre Sales [exist]  │  Platform Sales [exist]        │
├───────────────────────┴────────────────────────────────┤
│  Genre by Era [existing]                               │
├───────────────────────┬────────────────────────────────┤
│  Genre Critic [exist] │  (space for bubble if added)   │
├───────────────────────┬────────────────────────────────┤
│  [N3] Developer Sales │  [N4] Publisher Longevity      │
│        Bar  ← NEW     │        Scatter  ← NEW          │
└───────────────────────┴────────────────────────────────┘
```

### Page 3 — Regional & Ratings Analysis

```
┌────────────────────────────────────────────────────────┐
│  Title + Filters                                       │
├────────────────────────────────────────────────────────┤
│  Regional by Genre [existing]                          │
├───────────────────────┬────────────────────────────────┤
│  Critic vs Sales      │  Score Gap Histogram           │
│  [existing]           │  [existing]                    │
├────────────────────────────────────────────────────────┤
│  [N5] Score Gap by Genre (Diverging Bar)   ← NEW     │
├────────────────────────────────────────────────────────┤
│  [N6] ESRB Rating × Regional Sales (100%) ← NEW     │
└────────────────────────────────────────────────────────┘
```

---

## Filters — What You Need to Know

All 6 new charts use **separate pre-aggregated CSV files**, not the main `video_games_cleaned.csv`.  
This means they will **NOT** be controlled by the existing Era / Genre / Platform / Rating filter widgets (those only affect the main CSV).

**This is intentional** — the new charts serve as **fixed reference panels** that always show the full-dataset picture, while the existing charts respond to filters. This gives users two views simultaneously: the filtered view (existing charts) and the full-context view (new charts).

If you want a new chart to respond to filters, you have two options:
1. **Re-source it from `video_games_cleaned.csv`** and build the aggregation via Tableau calculated fields (the guide above's charts are pre-aggregated for simplicity).
2. **Add a Parameter Action** that syncs a filter value from the main CSV sheets to the new sheets.

---

## Generated Data Files Reference

| File | Columns | Rows | Used In |
|---|---|---|---|
| `yoy_growth.csv` | Year_of_Release, Global_Sales, YoY_Growth_Pct | 37 | N1 |
| `platform_timeline.csv` | Platform, First_Year, Last_Year, Lifespan_Years, Total_Sales, Avg_Critic_Score | 31 | N2 |
| `developer_kpi.csv` | Developer, Total_Sales, Avg_Critic_Score, Avg_User_Score, Title_Count | ~800 | N3 |
| `publisher_longevity.csv` | Publisher, Years_Active, First_Year, Last_Year, Total_Sales, Avg_Critic_Score, Title_Count | ~580 | N4 |
| `score_gap_by_genre.csv` | Genre, Game_Count, Avg_Score_Gap, Median_Score_Gap, Std_Score_Gap, Critic_Higher_Pct, User_Higher_Pct | 12 | N5 |
| `rating_region.csv` | Rating, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales, Title_Count | 9 | N6 |
