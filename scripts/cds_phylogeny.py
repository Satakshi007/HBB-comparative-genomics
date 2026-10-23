from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator

# Read the CDS alignment
alignment = AlignIO.read(
    "results/hbb_cds_alignment.aln",
    "clustal"
)

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

print("CDS PAIRWISE DISTANCE MATRIX")
print("----------------------------")
print(distance_matrix)

output_file = "results/cds_distance_matrix.txt"

with open(output_file, "w") as output:
    output.write("CDS PAIRWISE DISTANCE MATRIX\n")
    output.write("----------------------------\n")
    output.write(str(distance_matrix))
    output.write("\n")

print(f"\nResults saved to: {output_file}")
