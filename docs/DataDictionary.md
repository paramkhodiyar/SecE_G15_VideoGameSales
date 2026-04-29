# Data Dictionary — Video Game Sales & Market Trends
> SecE_G15 · Newton School of Technology · DVA Capstone 2
 

## Dataset Summary
| Item | Details |
|---|---|
| Dataset name | Video Game Sales |
| Source | Raw dataset (Kaggle) |
| Raw file name | `raw_dataset.csv` |
| Last updated | 2026-04-20 |
| Granularity | One row per video game release per platform |

## Column Definitions
| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| `Name` | string | The name of the video game | Wii Sports | EDA / Tableau | Dropped 2 nulls (primary identifier). Stripped whitespace, title cased. |
| `Platform` | string | The console/platform the game was released on | Wii | EDA / KPI / Tableau | Stripped whitespace, title cased. |
| `Year_of_Release` | int | The year the game was released | 2006 | EDA / KPI / Tableau | Nulls (269) replaced with median (2007). Capped range 1980–2016. |
| `Genre` | string | The genre of the video game | Sports | EDA / KPI / Tableau | Stripped whitespace, title cased. |
| `Publisher` | string | The publisher of the video game | Nintendo | EDA / Tableau | Stripped whitespace, title cased. |
| `Developer` | string | The developer studio of the video game | Nintendo | EDA / Tableau | Stripped whitespace, title cased. Null strings normalized. |
| `Rating` | string | The ESRB rating of the game | E | EDA / Tableau | Stripped whitespace, title cased. |
| `NA_Sales` | float | Sales in North America (in millions) | 41.36 | KPI / Tableau | Nulls set to 0. |
| `EU_Sales` | float | Sales in Europe (in millions) | 28.96 | KPI / Tableau | Nulls set to 0. |
| `JP_Sales` | float | Sales in Japan (in millions) | 3.77 | KPI / Tableau | Nulls set to 0. |
| `Other_Sales` | float | Sales in the rest of the world (in millions) | 8.45 | KPI / Tableau | Nulls set to 0. |
| `Global_Sales` | float | Total worldwide sales (in millions) | 82.53 | EDA / KPI / Tableau | - |
| `Critic_Score` | float | Aggregate score compiled by Metacritic (out of 100) | 76.0 | EDA / Tableau | Nulls filled with column median. Cast to float. |
| `Critic_Count` | int | Number of critics used in calculating the score | 51 | EDA | Nulls filled with column median. Cast to int. |
| `User_Score` | float | Score given by users (out of 10) | 8.0 | EDA / Tableau | 'tbd' entries (2424) replaced with nulls, then filled with median (7.50). |
| `User_Count` | int | Number of users who gave a score | 322 | EDA | Nulls filled with column median. Cast to int. |

## Derived Columns
| Derived Column | Logic | Business Meaning |
|---|---|---|
| `Global_Sales_Calculated` | `NA_Sales` + `EU_Sales` + `JP_Sales` + `Other_Sales` | Used to cross-validate the original `Global_Sales` column and check for inconsistencies. |
| `Sales_Region_Dominant` | Region with the highest sales value | Identifies the strongest market for each specific game release. |
| `Era` | Groups `Year_of_Release` into decades (e.g., 2000s, 1980s) | Allows for high-level grouping and temporal analysis of industry trends across decades. |
| `Score_Gap` | `Critic_Score` - (`User_Score` * 10) | Highlights discrepancies between critic reception and user reception. |

## Data Quality Notes
- **Year Capping**: Release years were capped strictly between 1980 and 2016. Games outside this range were removed.
- **Score Imputation**: Large numbers of missing scores (`Critic_Score`, `User_Score`, etc.) were filled with the median. This may artificially cluster analysis around the median for games without true Metacritic data.
- **'tbd' User Scores**: 2,424 User_Score entries marked as 'tbd' were treated as null and also filled with the median (7.5).
- **Missing Names**: 2 rows lacking a game `Name` were dropped entirely, as `Name` serves as the primary record identifier.
- **Null Sales**: Any null values in regional sales were filled with 0.