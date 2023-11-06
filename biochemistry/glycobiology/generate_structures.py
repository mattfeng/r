import os

from rdkit import Chem
from io import BytesIO
from rdkit.Chem import AllChem, Draw, rdDepictor
from PIL import Image
from cairosvg import svg2png

def draw_molecules_from_smiles(smiles_list, output_dir, size=(300, 300)):
    for idx, (legend, smiles) in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(smiles)

        if mol is not None:
            rdDepictor.Compute2DCoords(mol)
            rdDepictor.StraightenDepiction(mol)

            d2d = Draw.MolDraw2DSVG(-1, -1)
            Draw.SetACS1996Mode(d2d.drawOptions(), Draw.MeanBondLength(mol))
            dopts = d2d.drawOptions()
            dopts.useCDKAtomPalette()
            dopts.fontFile = "BuiltinTelexRegular"
            dopts.bondLineWidth = 0.8
            dopts.legendFontSize = 10
            dopts.additionalAtomLabelPadding = 0.15

            d2d.DrawMolecule(mol)
            d2d.FinishDrawing()

            svg_text = d2d.GetDrawingText()

            svg2png(
                bytestring=svg_text,
                dpi=600,
                scale=6,
                write_to=os.path.join(output_dir, f"{legend}.png")
                )


# Example usage:
smiles_list = [
    ("4eLeg", "C[C@H]([C@H]([C@H]1[C@@H]([C@@H](C[C@](O1)(C(=O)O)O)O)N)N)O")
]

output_dir = "output_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

draw_molecules_from_smiles(smiles_list, output_dir)