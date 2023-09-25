# NCBI Database Queries

## Entrez queries

### Specify the organism you want to get sequences for

```
<query> AND <organism>[organism]

# e.g. human
<query> AND human[organism]
```

- `<organism>`
    - can be a description of an organism or a NCBI Taxonomy ID (see the [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi))

## References

1. Entrez Help: https://www.ncbi.nlm.nih.gov/books/NBK3837/
2. Query tips: https://www.ncbi.nlm.nih.gov/homologene/query-tips/

```
[Ancestor]	Taxonomic name of common ancestor of the species represented in a HomoloGene entry.
[Gene Description]	Detailed description of a Gene.
[Gene Id]	Unique Gene Identifier.
[Gene Name]	Gene Aliases.
[Nucleotide Accession]	GenBank accession identifier of nucleotide sequence.
[Nucleotide GI]	Unique Nucleotide identifier.
[Organism]	Description of the organism or the NCBI Taxonomy ID of a species.
[Protein Accession]	The protein accession number of a protein.
[Protein GI]	Unique Protein identifier.
[Text Word]	Free text to be searched for in HomoloGene.
[Title]	Summary of HomoloGene entry
[UniGene ID]	Unique Unigene identifier.
```
