from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Phylo
import matplotlib.pyplot as plt

alignment = AlignIO.read("results/alignment.aln", "fasta")

for record in alignment:
    if record.id == "XM_508242.5":
        record.id = "Chimpanzee"
    elif record.id == "NM_173917.2":
        record.id = "Cow"
    elif record.id == "NM_000518.5":
        record.id = "Human"
    elif record.id == "NM_001278161.1":
        record.id = "Mouse"

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

print(distance_matrix)

constructor = DistanceTreeConstructor()
tree = constructor.nj(distance_matrix)
Phylo.draw_ascii(tree)
with open("results/distance_matrix.txt", "w") as f:
    f.write(str(distance_matrix))

plt.figure(figsize=(6,8))
Phylo.draw(tree, do_show=False)
plt.tight_layout()
plt.savefig("results/phylogenetic_tree.png", dpi=300)
plt.show()

print("Phylogenetic tree saved as 'results/phylogenetic_tree.png'") 
print("Distance matrix saved as 'results/distance_matrix.txt'")