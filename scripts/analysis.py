from Bio import AlignIO
alignment = AlignIO.read("results/alignment.aln", "fasta")

print("Sequences:", len(alignment))
print("Length:", alignment.get_alignment_length())

#count conserved positions
from Bio import AlignIO

alignment = AlignIO.read("results/alignment.aln", "fasta")

length = alignment.get_alignment_length()
conserved = 0

for i in range(length):
    column = alignment[:, i]

    if len(set(column)) == 1:
        conserved += 1

print("Alignment length:", length)
print("Conserved positions:", conserved)
print("Conservation percentage:", conserved/length*100)

#count variable positions
variable = length - conserved
print("Variable positions:", variable)\

#Gap analysis
for record in alignment:
    gaps = record.seq.count("-")
    print(record.id, "Gaps:", gaps)