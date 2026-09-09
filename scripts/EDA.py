import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
matches = pd.read_csv(os.path.join(BASE_DIR, '..', 'output', 'cleaned_matches.csv'))
deliveries = pd.read_csv(os.path.join(BASE_DIR, '..', 'output', 'cleaned_deliveries.csv'))

CHART_DIR = os.path.join(BASE_DIR, '..', 'output', 'charts')
os.makedirs(CHART_DIR, exist_ok=True)

print("=== DESCRIPTIVE STATISTICS ===")
print(matches[['win_by_runs', 'win_by_wickets']].describe())
print("\nTotal runs scored across all deliveries:", deliveries['total_runs'].sum())
print("Matches per season:\n", matches['season'].value_counts().sort_index())

print("\n=== TOP 10 RUN SCORERS ===")
top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print(top_batsmen)

print("\n=== TOP 10 WICKET TAKERS ===")
# only dismissals credited to the bowler (excludes run outs)
bowler_dismissals = deliveries[deliveries['dismissal_kind'].isin(
    ['caught', 'bowled', 'lbw', 'stumped', 'caught and bowled', 'hit wicket']
)]
top_bowlers = bowler_dismissals.groupby('bowler')['player_dismissed'].count().sort_values(ascending=False).head(10)
print(top_bowlers)

print("\n=== TOSS DECISION IMPACT ===")
matches['toss_match_winner_same'] = matches['toss_winner'] == matches['winner']
print(matches['toss_decision'].value_counts())
print("\nToss winner also won match:")
print(matches['toss_match_winner_same'].value_counts(normalize=True) * 100)

print("\n=== CORRELATION (numeric fields) ===")
print(matches[['win_by_runs', 'win_by_wickets', 'dl_applied']].corr())

# --- Chart 1: Matches per season ---
plt.figure(figsize=(9, 5))
matches['season'].value_counts().sort_index().plot(kind='bar', color='#1E2761')
plt.title('IPL Matches Played Per Season (2008-2017)')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, 'matches_per_season.png'), dpi=120)
plt.close()

# --- Chart 2: Win margin distribution (boxplot) ---
plt.figure(figsize=(7, 5))
matches[matches['win_by_runs'] > 0]['win_by_runs'].plot(kind='box')
plt.title('Distribution of Win Margins (by Runs)')
plt.ylabel('Runs')
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, 'win_margin_boxplot.png'), dpi=120)
plt.close()

# --- Chart 3: Top 10 run scorers ---
plt.figure(figsize=(9, 5))
top_batsmen.sort_values().plot(kind='barh', color='#E8A33D')
plt.title('Top 10 Run Scorers (2008-2017)')
plt.xlabel('Total Runs')
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, 'top_10_batsmen.png'), dpi=120)
plt.close()

# --- Chart 4: Toss decision split (pie) ---
plt.figure(figsize=(6, 6))
matches['toss_decision'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#1E2761', '#E8A33D'])
plt.title('Toss Decision: Bat vs Field')
plt.ylabel('')
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, 'toss_decision_pie.png'), dpi=120)
plt.close()

print("\nSaved 4 charts to output/charts/")