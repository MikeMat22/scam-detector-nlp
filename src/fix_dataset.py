import pandas as pd
import os

# Cesta ke vstupnímu souboru
input_path = "data/SMSSpamCollection"  # nebo změň podle potřeby
output_path = "data/clean_messages.csv"

# Načti data (původní dataset je tab-delimited!)
df = pd.read_csv(input_path, sep='\t', header=None, names=["label", "message"], encoding='utf-8')

# Odstraň prázdné zprávy
df.dropna(inplace=True)

# Zkontroluj počet unikátních labelů
print("✅ Labely v datasetu:", df["label"].unique())
print("📊 Rozložení labelů:\n", df["label"].value_counts())

# Ulož čistý dataset
df.to_csv(output_path, index=False)

print(f"\n✅ Dataset byl úspěšně očištěn a uložen do: {output_path}")