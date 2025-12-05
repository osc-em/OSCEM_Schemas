
# Class: Ligand

Information on ligands if present.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Ligand](https://w3id.org/osc-em/oscem-schemas-subtomo/Ligand)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Sample]++-%20ligands%200..*>[Ligand&#124;present:boolean%20%3F;smiles:string%20%3F;reference:string%20%3F],[Sample]++-%20ligands(i)%200..*>[Ligand])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Sample]++-%20ligands%200..*>[Ligand&#124;present:boolean%20%3F;smiles:string%20%3F;reference:string%20%3F],[Sample]++-%20ligands(i)%200..*>[Ligand])

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞ligands](Sample_ligands.md)*  <sub>0..\*</sub>  **[Ligand](Ligand.md)**
 *  **None** *[ligands](ligands.md)*  <sub>0..\*</sub>  **[Ligand](Ligand.md)**

## Attributes


### Own

 * [Ligand➞present](Ligand_present.md)  <sub>0..1</sub>
     * Description: Whether the model contains any ligands
     * Range: [Boolean](types/Boolean.md)
 * [smiles](smiles.md)  <sub>0..1</sub>
     * Description: Provide a valid SMILES string of your ligand
     * Range: [String](types/String.md)
 * [reference](reference.md)  <sub>0..1</sub>
     * Description: Link to a reference of your ligand, i.e., CCD, PubChem, etc.
     * Range: [String](types/String.md)
