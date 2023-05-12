import pandas as pd
import pydawg

df = pd.read_csv(
    "CID-Synonym-filtered.gz",
    compression="gzip",
    sep="\t",
    names=["cid", "synonym"],
)

df["synonym"] = df["synonym"].str.strip()
df["synonym"] = df["synonym"].str.lower()
df = df.sort_values("synonym")

chem_tagger = pydawg.DAWG()

for key in df["synonym"].values:
    ee = chem_tagger.add_word_unchecked(key)

with open("chem_dict", "wb") as f:
    f.write(chem_tagger.bindump())
