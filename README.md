# IPL Data Analytics (2008–2017)

End-to-end data analytics project on IPL match data — cleaning, exploratory analysis, SQL-based business analysis, and an interactive Power BI dashboard.

**Dataset:** 636 matches, 150,460 ball-by-ball deliveries (source: Kaggle IPL dataset via GitHub mirror)

## Stage 1: Data Cleaning (`scripts/Cleaning.py`)
- Fixed team name inconsistency (Rising Pune Supergiant/Supergiants)
- Handled missing values in city, winner, player_of_match, umpires
- Removed 1 duplicate delivery record
- Dropped umpire3 column (100% empty)

## Stage 2: Exploratory Data Analysis (`scripts/EDA.py`)
- Descriptive stats, top run scorers, top wicket takers
- Toss decision impact analysis (toss winner won match only 51% of the time)
- 4 charts: matches per season, win margin distribution, top 10 batsmen, toss decision split

## Stage 3: SQL Analysis (PostgreSQL, `scripts/*.sql`)
- Team wins, venue analysis, toss impact, top scorers, season-wise run trends
- All queries verified against Python results

## Stage 4: Visualization (Power BI, `IPL_Dashboard.pbix`)
- Interactive dashboard: total runs, matches played, unique players, wins by team, runs trend by season, toss split, top 10 run scorers

## Tools
Python (Pandas, Matplotlib) · PostgreSQL · Power BI · Git/GitHub