
# Class: SampleMolecular



URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-general/SampleMolecular](https://w3id.org/oscem-schemas/latest/oscem-schemas-general/SampleMolecular)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[OverallMolecule]<overall_molecule%201..1-++[SampleMolecular&#124;name:string%20%3F;description:string%20%3F],[Sample]^-[SampleMolecular],[Sample],[OverallMolecule],[Molecule],[Ligand],[Grid])](https://yuml.me/diagram/nofunky;dir:TB/class/[Specimen],[OverallMolecule]<overall_molecule%201..1-++[SampleMolecular&#124;name:string%20%3F;description:string%20%3F],[Sample]^-[SampleMolecular],[Sample],[OverallMolecule],[Molecule],[Ligand],[Grid])

## Parents

 *  is_a: [Sample](Sample.md) - Unifying class to describe the full sample.

## Referenced by Class


## Attributes


### Own

 * [SampleMolecular➞name](SampleMolecular_name.md)  <sub>0..1</sub>
     * Description: The name of the item
     * Range: [String](types/String.md)
 * [SampleMolecular➞description](SampleMolecular_description.md)  <sub>0..1</sub>
     * Description: The description of the item
     * Range: [String](types/String.md)
 * [SampleMolecular➞overall_molecule](SampleMolecular_overall_molecule.md)  <sub>1..1</sub>
     * Description: Description of the overall molecule
     * Range: [OverallMolecule](OverallMolecule.md)

### Inherited from Sample:

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
