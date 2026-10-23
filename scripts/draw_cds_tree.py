from Bio import Phylo
import matplotlib.pyplot as plt

tree = Phylo.read("results/hbb_cds_tree.contree", "newick")

fig, ax = plt.subplots(figsize=(10, 6))

Phylo.draw(
    tree,
    axes=ax,
    do_show=False,
    branch_labels=lambda clade: (
        str(clade.confidence)
        if clade.confidence is not None
        else None
    )
)

ax.set_title("HBB CDS Phylogenetic Tree")
ax.set_xlabel("Estimated substitutions per site")

plt.tight_layout()

plt.savefig(
    "results/hbb_cds_phylogenetic_tree.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Tree saved to results/hbb_cds_phylogenetic_tree.png")
