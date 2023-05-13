# Simple chemical tagger with PubChem synonyms and pyDAWG

Install [pyDAWG](https://github.com/WojciechMula/pyDAWG) and pandas

- pip install https://github.com/WojciechMula/pyDAWG/archive/master.zip
- pip install pandas

It needs a C compiler since pyDAWG builds a Python C extension

## Dictionary of synonyms

Download Download PubChem synonyms (ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-Synonym-filtered.gz) and run [gen_file.py](https://github.com/eloyfelix/chem_tagger/blob/main/gen_file.py)


or download the pre-calculated dictionary from [here](https://ftp.ebi.ac.uk/pub/databases/chembl/other/chem_dict.gz)

## Quick test with ChEMBL synonyms

Loading the dictionary takes ~2minutes. Once it is loaded it takes 0.4 seconds to tag 260000 synonyms from ChEMBL.

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
