
# Class: Sample

Unifying class to describe the full sample.

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Sample](https://w3id.org/osc-em/oscem-schemas-spa/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[Grid]<grid%200..1-++[Sample],[Specimen]<specimen%201..1-++[Sample],[Ligand]<ligands%200..*-++[Sample],[Molecule]<molecule%201..*-++[Sample],[OverallMolecule]<overall_molecule%201..1-++[Sample],[EMDatasetSpa]++-%20sample%200..1>[Sample],[OverallMolecule],[Molecule],[Ligand],[Grid],[EMDatasetSpa])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[Grid]<grid%200..1-++[Sample],[Specimen]<specimen%201..1-++[Sample],[Ligand]<ligands%200..*-++[Sample],[Molecule]<molecule%201..*-++[Sample],[OverallMolecule]<overall_molecule%201..1-++[Sample],[EMDatasetSpa]++-%20sample%200..1>[Sample],[OverallMolecule],[Molecule],[Ligand],[Grid],[EMDatasetSpa])

## Referenced by Class

 *  **[EMDatasetSpa](EMDatasetSpa.md)** *[EMDatasetSpa➞sample](EMDatasetSpa_sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [Sample➞overall_molecule](Sample_overall_molecule.md)  <sub>1..1</sub>
     * Description: Description of the overall molecule
     * Range: [OverallMolecule](OverallMolecule.md)
 * [Sample➞molecule](Sample_molecule.md)  <sub>1..\*</sub>
     * Description: List of molecule associated with the sample
     * Range: [Molecule](Molecule.md)
 * [Sample➞ligands](Sample_ligands.md)  <sub>0..\*</sub>
     * Description: List of ligands associated with the sample
     * Range: [Ligand](Ligand.md)
 * [Sample➞specimen](Sample_specimen.md)  <sub>1..1</sub>
     * Description: Description of the specimen
     * Range: [Specimen](Specimen.md)
 * [Sample➞grid](Sample_grid.md)  <sub>0..1</sub>
     * Description: Description of the grid used
     * Range: [Grid](Grid.md)
