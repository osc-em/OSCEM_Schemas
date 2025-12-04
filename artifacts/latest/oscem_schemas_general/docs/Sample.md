
# Class: Sample

Unifying class to describe the full sample.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-general/Sample](https://w3id.org/oscem-schemas/latest/oscem-schemas-general/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[SampleMolecular],[Grid]<grid%200..1-++[Sample&#124;name:string;description:string],[Specimen]<specimen%200..1-++[Sample],[Ligand]<ligands%200..*-++[Sample],[Molecule]<molecule%200..*-++[Sample],[OverallMolecule]<overall_molecule%200..1-++[Sample],[EMDatasetGeneral]++-%20sample%200..1>[Sample],[Sample]^-[SampleMolecular],[OverallMolecule],[Molecule],[Ligand],[Grid],[EMDatasetGeneral])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[SampleMolecular],[Grid]<grid%200..1-++[Sample&#124;name:string;description:string],[Specimen]<specimen%200..1-++[Sample],[Ligand]<ligands%200..*-++[Sample],[Molecule]<molecule%200..*-++[Sample],[OverallMolecule]<overall_molecule%200..1-++[Sample],[EMDatasetGeneral]++-%20sample%200..1>[Sample],[Sample]^-[SampleMolecular],[OverallMolecule],[Molecule],[Ligand],[Grid],[EMDatasetGeneral])

## Children

 * [SampleMolecular](SampleMolecular.md)

## Referenced by Class

 *  **[EMDatasetGeneral](EMDatasetGeneral.md)** *[EMDatasetGeneral➞sample](EMDatasetGeneral_sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [Sample➞name](Sample_name.md)  <sub>1..1</sub>
     * Description: The name of the item
     * Range: [String](types/String.md)
 * [Sample➞description](Sample_description.md)  <sub>1..1</sub>
     * Description: The description of the item
     * Range: [String](types/String.md)
 * [Sample➞overall_molecule](Sample_overall_molecule.md)  <sub>0..1</sub>
     * Description: Description of the overall molecule
     * Range: [OverallMolecule](OverallMolecule.md)
 * [Sample➞molecule](Sample_molecule.md)  <sub>0..\*</sub>
     * Description: List of molecule associated with the sample
     * Range: [Molecule](Molecule.md)
 * [Sample➞ligands](Sample_ligands.md)  <sub>0..\*</sub>
     * Description: List of ligands associated with the sample
     * Range: [Ligand](Ligand.md)
 * [Sample➞specimen](Sample_specimen.md)  <sub>0..1</sub>
     * Description: Description of the specimen
     * Range: [Specimen](Specimen.md)
 * [Sample➞grid](Sample_grid.md)  <sub>0..1</sub>
     * Description: Description of the grid used
     * Range: [Grid](Grid.md)
