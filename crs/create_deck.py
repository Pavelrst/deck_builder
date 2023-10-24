from save_to_pdf import save_cards_to_pdf
from process_card import create_card
from tqdm import tqdm
import pandas as pd
import os
from constants import (
    NAME,
    ATTACK,
    DEFENCE,
    SPECIAL,
    FILENAME,
    DIR,
    OUTPUT_PDF,
)


df = pd.read_excel("data/database.xlsx")
card_paths = []
for i, row in tqdm(df.iterrows()):
    image_path = os.path.join(DIR, row[FILENAME])
    create_card(image_path,
                name=row[NAME],
                attack=row[ATTACK],
                defence=row[DEFENCE],
                special="\n\n".join(row[SPECIAL].split("#")),
                output_path=f"data/temp_files/temp{i}.png")
    card_paths.append(f"data/temp_files/temp{i}.png")

print(f"Save cards to PDF")
save_cards_to_pdf(OUTPUT_PDF, card_paths)
