# Comparative Genomic Analysis of the Haemoglobin Beta(HBB) Gene across Vertebrate Species
## Project Overview
This project compares the Haemoglobin beta(HBB) mRNA gene across four selected vertebrate species. Both full mRNA sequences and coding DNA sequences (CDS) were analysed using multiple sequence alignment, sequence conservation analysis, pairwise distance calculations, and phylogenetic analysis.
## Species Analyzed
- *Homo sapiens* (Human)
- *Pan troglodytes* (Chimpanzee) [Predicted Refseq]
- *Bos taurus* (Cow)
- *Mus musculus* (Mouse)
## Tools Used
- WSL2 (Ubuntu/Linux)
- Bash
- Clustal Omega
- Python
- Biopython
- Git & Github
- VS Code
- IQ- TREE
## Repository Structure
- data/ - Input FASTA sequence from NCBI
- scripts/ - Python analysis scripts
- results/ - Alignment, Distance matrix, Phylogenetic tree
- report/ - Detailed project report
- README.md - Project overview
## Results 
1. Full mRNA Sequence Analysis

The multiple sequence alignment of the four full mRNA sequences produced the following results:
- Number of Sequences = 4
- Alignment length = 657bp
- Conserved positions = 403
- Variable positions = 254
- Conservation = 61.34%
### Phylogenetic Tree
![Phylogenetic tree](results/phylogenetic_tree.png)
The phylogenetic analysis clustered Human and Chimpanzee together indicating high sequence similarity, while Cow and Mouse formed more distant branch.


2. Coding DNA Sequence (CDS) Analysis

The coding regions were extracted and analysed separately to examine conservation within the protein-coding portions of the gene.

- Number of sequences: 4
- Alignment length: 444 nucleotide columns
- Conserved positions: 326
- Variable positions: 118
- Conserved positions: 73.42%

The CDS alignment was also analysed using IQ-TREE. ModelFinder selected the Kimura two-parameter (K2P) substitution model, and phylogenetic analysis was performed with 1,000 ultrafast bootstrap replicates.

3. Bootstrap Analysis

Bootstrap analysis was performed using IQ-TREE to assess support for the phylogenetic relationships inferred from the full mRNA sequences and CDS alignment.

Bootstrap support provides an indication of how consistently a grouping appears when alignment columns are resampled. 
## How to Run
Full mRNA analysis
- for running alignment
  - clustalo -i data/hbb_all.fasta -o results/alignment.aln
- python scripts/analysis.py 
- python scripts/phylogeny.py
CDS Analysis
- python scripts/extract_cds.py
- python scripts/cds_analysis.py
- python scripts/cds_phylogeny.py
- python scripts/draw_cds_tree.py
## Future Improvement
- Include additional species.
- Visualise conserved and variable sequence regions.
- Investigate the effects of alignment methods and substitution models on phylogenetic results.
- Expand the analysis using codon-aware alignment methods.
- Calculate sequence identity percentages.
- Extend the study to other globin genes.
### Author
Satakshi
