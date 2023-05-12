# Simple chemical tagger with PubChem synonyms and pyDAWG

Download PubChem synonyms from ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-filtered.gz and install [pyDAWG](https://github.com/WojciechMula/pyDAWG)

- pip install https://github.com/WojciechMula/pyDAWG/archive/master.zip

It needs a C compiler since it builds a Python C extension

## Create dictionary of synonyms

run gen_file.py (or download the pre-calculated dict from [here](https://ftp.ebi.ac.uk/pub/databases/chembl/other/chem_dict.gz))

## Quick test with ChEMBL synonyms

```python
import pydawg

chem_tagger = pydawg.DAWG()

with open("chem_dict", "rb") as f:
    chem_tagger.binload(f.read())

result = []
with open("chembl_synonyms.txt") as f:
    for line in f:
        result.append(chem_tagger.exists(line.strip().lower()))

print(sum(result)/len(result))
```
