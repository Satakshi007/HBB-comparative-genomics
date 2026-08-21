# Comparative Genomic Analysis of Haemoglobin Beta (HBB) mRNA Gene Across Selected Vertebrate Species
Author: Satakshi  
Course: BSc (Hons.) Bioinformatics

## 1. Introduction
- Haemoglobin:  
  Haemoglobin is a globular protein found in red blood cells of vertebrates. It contains iron, which enables it to transport oxygen from the respiratory organs to body tissues. This oxygen delivery supports aerobic respiration and metabolic activity. In mammals, haemoglobin is a tetramer made of two alpha and two beta globin chains, each containing a heme group with an iron atom that binds oxygen.

- HBB Gene:  
  The haemoglobin beta (HBB) gene encodes the beta-globin protein. In humans, this gene is located on chromosome 11. Mutations in HBB are associated with disorders such as sickle-cell disease and beta-thalassemia, which makes the gene highly significant in molecular biology and clinical genetics.

- Comparative Genomics:  
  Comparative genomics involves comparing genomic sequences across species to identify similarities, differences, and evolutionary relationships. This approach helps reveal conserved regions that are functionally important and variable regions that may reflect evolutionary divergence.

- Why HBB?  
  HBB is a suitable target for comparative analysis because it is functionally conserved across vertebrates, yet its nucleotide sequence still varies due to evolutionary changes. Studying HBB sequences across species can therefore help infer both conservation patterns and phylogenetic relationships.

In this study, HBB mRNA sequences from Human (*Homo sapiens*), Chimpanzee (*Pan troglodytes*), Cow (*Bos taurus*), and Mouse (*Mus musculus*) were retrieved from the NCBI database. Multiple sequence alignment was performed using Clustal Omega, followed by conservation analysis and phylogenetic tree construction using Python and Biopython. The results were used to investigate sequence conservation and evolutionary relationships among the selected vertebrate species.

## 2. Objectives
- To retrieve HBB mRNA sequences of the selected vertebrate species from the NCBI database.
- To perform multiple sequence alignment (MSA) using Clustal Omega.
- To identify conserved and variable nucleotide positions in the aligned sequences.
- To calculate conservation percentage and analyze gap distribution across sequences.
- To determine the evolutionary relationship among the selected species using phylogenetic analysis.
- To demonstrate the application of bioinformatics tools in comparative genomics and molecular evolution studies.

## 3. Materials and Methods
### 3.1 Data Collection
HBB mRNA sequences of Human (*Homo sapiens*, NM_000518.5), Chimpanzee (*Pan troglodytes*, XM_508242.5), Cow (*Bos taurus*, NM_173917.2), and Mouse (*Mus musculus*, NM_001278161.1) were retrieved from the NCBI Gene database in FASTA format. The Human, Cow, and Mouse records were experimentally derived, while the Chimpanzee sequence was predicted.

### 3.2 Software and Tools
| Software/Tool | Purpose |
| --- | --- |
| WSL2 (Ubuntu Linux) | Linux environment |
| Visual Studio Code | Code editor |
| Bash | Command-line interface |
| Python 3 | Data analysis |
| Biopython | Sequence and phylogenetic analysis |
| Clustal Omega | Multiple sequence alignment |
| Git & GitHub | Version control and project management |

### 3.3 Multiple Sequence Alignment
Multiple sequence alignment was performed in the WSL Ubuntu environment using Clustal Omega through the Bash command line. The aligned sequences were exported in FASTA format and saved as `results/alignment.aln` for downstream analysis.

Command used:
```bash
clustalo -i data/hbb_all.fasta -o results/alignment.aln --outfmt=fasta --force
```

### 3.4 Conservation Analysis
The aligned sequences were analyzed using a Python script developed with Biopython. The script calculated:
- Total number of sequences
- Alignment length
- Conserved positions
- Variable positions
- Conservation percentage
- Gap count for each sequence

### 3.5 Phylogenetic Analysis
Pairwise sequence distances were calculated using the identity distance model in Biopython, and a neighbor-joining phylogenetic tree was constructed from the resulting distance matrix. This was used to infer evolutionary relationships among the selected vertebrate sequences.

## 4. Results
### 4.1 Alignment Summary
The final multiple sequence alignment contained four HBB mRNA sequences with a total alignment length of 657 nucleotides. The alignment showed several conserved regions shared among all species, together with variable sites and gaps, indicating both sequence similarity and evolutionary divergence.

### 4.2 Conservation Result
From the verified analysis output:
- Number of sequences: 4
- Alignment length: 657 bp
- Conserved positions: 403
- Variable positions: 254
- Conservation percentage: 61.34%

Gap counts per sequence were:
- Chimpanzee: 18 gaps
- Cow: 24 gaps
- Human: 29 gaps
- Mouse: 27 gaps

These results suggest that the HBB gene is moderately conserved across the selected species, while the remaining positions reflect nucleotide substitutions and indel events.

### 4.3 Gap Analysis
 Gap analysis of the multiple sequence alignment showed the presence of insertion/deletion sites among the aligned HBB mRNA sequences. The number of gaps varied among the four selected species. Chimpanzee had the lowest number of gaps (18), while Human had the highest number of gaps (29). Cow and Mouse contained 24 and 27 gaps, respectively.

 | Species                        | Number of Gaps |
| ------------------------------ | -------------: |
| Chimpanzee (*Pan troglodytes*) |             18 |
| Cow (*Bos taurus*)             |             24 |
| Human (*Homo sapiens*)         |             29 |
| Mouse (*Mus musculus*)         |             27 |

These gaps were distributed at different positions within the alignment and were observed as - characters in the aligned sequences.

### 4.4 Distance Matrix
Pairwise sequence distances were calculated for the aligned HBB mRNA sequences using the identity distance model in Biopython. The resulting distance matrix is shown below.

|                | Chimpanzee |      Cow |    Human |    Mouse |
| -------------- | ---------: | -------: | -------: | -------: |
| **Chimpanzee** |   0.000000 |        — |        — |        — |
| **Cow**        |   0.242009 | 0.000000 |        — |        — |
| **Human**      |   0.018265 | 0.225266 | 0.000000 |        — |
| **Mouse**      |   0.245053 | 0.328767 | 0.234399 | 0.000000 |

The lowest pairwise distance was observed between Human and Chimpanzee (0.018265). The highest pairwise distance was observed between Cow and Mouse (0.328767).

### 4.5 Phylogenetic Tree and Relationship
The distance matrix generated from the alignment showed the lowest distance between Human and Chimpanzee, indicating a very close evolutionary relationship. The pairwise distance values were:
- Human–Chimpanzee: 0.018265
- Human–Cow: 0.225266
- Human–Mouse: 0.234399
- Chimpanzee–Cow: 0.242009
- Chimpanzee–Mouse: 0.245053
- Cow–Mouse: 0.328767

The neighbor-joining tree grouped Human and Chimpanzee together, while Cow and Mouse formed more distant branches. This pattern is consistent with the expected evolutionary proximity between the human and chimpanzee sequences.

![Phylogenetic Tree](../results/phylogenetic_tree.png)

**Figure 1.** Neighbor-Joining phylogenetic tree constructed from HBB mRNA sequences.

## 5. Discussion and Conclusion
The comparative analysis of HBB mRNA sequences across Human, Chimpanzee, Cow, and Mouse showed a strong overall similarity in the coding region, as evidenced by the high number of conserved nucleotide positions. The conservation percentage of 61.34% indicates that the gene remains functionally constrained, even though several variable and gap-containing positions reflect evolutionary divergence.

The phylogenetic tree further supports the close relationship between Human and Chimpanzee, while the greater pairwise distances of Cow and Mouse indicate deeper divergence. Overall, this study demonstrates the usefulness of multiple sequence alignment and phylogenetic analysis in exploring gene conservation and evolutionary relationships among vertebrate species.

## 6. References
- NCBI Gene database
- Biopython documentation
- Clustal Omega documentation
- Comparative genomics literature on globin gene evolution

