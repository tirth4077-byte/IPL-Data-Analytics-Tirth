import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
matches = pd.read_csv(os.path.join(BASE_DIR, '..', 'data', 'matches.csv'))
deliveries = pd.read_csv(os.path.join(BASE_DIR, '..', 'data', 'deliveries.csv'))

# --- Fix team name inconsistency ---
matches['team1'] = matches['team1'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')
matches['team2'] = matches['team2'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')
matches['winner'] = matches['winner'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')
matches['toss_winner'] = matches['toss_winner'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')
deliveries['batting_team'] = deliveries['batting_team'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')
deliveries['bowling_team'] = deliveries['bowling_team'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')

# --- Handle missing values ---
matches['city'] = matches['city'].fillna('Unknown')
matches['winner'] = matches['winner'].fillna('No Result')
matches['player_of_match'] = matches['player_of_match'].fillna('Not Awarded')
matches['umpire1'] = matches['umpire1'].fillna('Unknown')
matches['umpire2'] = matches['umpire2'].fillna('Unknown')
matches = matches.drop(columns=['umpire3'])   # 100% empty, no analytical value

# --- Duplicate check and removal ---
print("Duplicate rows -> matches:", matches.duplicated().sum(), " deliveries:", deliveries.duplicated().sum())
matches = matches.drop_duplicates()
deliveries = deliveries.drop_duplicates()

# --- Data type fix ---
matches['date'] = pd.to_datetime(matches['date'])

# --- Post-cleaning validation ---
print("\nPost-cleaning nulls in matches:", matches.isnull().sum().sum())
print("Final matches shape:", matches.shape)
print("Final deliveries shape:", deliveries.shape)

# --- Save cleaned files ---
matches.to_csv(os.path.join(BASE_DIR, '..', 'output', 'cleaned_matches.csv'), index=False)
deliveries.to_csv(os.path.join(BASE_DIR, '..', 'output', 'cleaned_deliveries.csv'), index=False)
print("\nSaved cleaned_matches.csv and cleaned_deliveries.csv to output/")