
# Class: OverallMolecule

Description of the overall molecule

URI: [https://w3id.org/osc-em/oscem-schemas-tomo/OverallMolecule](https://w3id.org/osc-em/oscem-schemas-tomo/OverallMolecule)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[QuantityValue],[QuantityValue]<molecular_weight%200..1-++[OverallMolecule&#124;molecular_overall_type:MoleculeClassEnum%20%3F;name_sample:string;source:string;assembly:AssemblyEnum%20%3F],[Sample]++-%20overall_molecule%201..1>[OverallMolecule],[Sample]++-%20overall_molecule(i)%200..1>[OverallMolecule])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[QuantityValue],[QuantityValue]<molecular_weight%200..1-++[OverallMolecule&#124;molecular_overall_type:MoleculeClassEnum%20%3F;name_sample:string;source:string;assembly:AssemblyEnum%20%3F],[Sample]++-%20overall_molecule%201..1>[OverallMolecule],[Sample]++-%20overall_molecule(i)%200..1>[OverallMolecule])

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞overall_molecule](Sample_overall_molecule.md)*  <sub>1..1</sub>  **[OverallMolecule](OverallMolecule.md)**
 *  **None** *[overall_molecule](overall_molecule.md)*  <sub>0..1</sub>  **[OverallMolecule](OverallMolecule.md)**

## Attributes


### Own

 * [OverallMolecule➞molecular_overall_type](OverallMolecule_molecular_overall_type.md)  <sub>0..1</sub>
     * Description: Description of the overall molecular type, i.e., a complex
     * Range: [MoleculeClassEnum](MoleculeClassEnum.md)
 * [OverallMolecule➞name_sample](OverallMolecule_name_sample.md)  <sub>1..1</sub>
     * Description: Name of the full sample
     * Range: [String](types/String.md)
 * [OverallMolecule➞source](OverallMolecule_source.md)  <sub>1..1</sub>
     * Description: Where the sample was taken from, i.e., natural host, recombinantly expressed, etc.
     * Range: [String](types/String.md)
 * [OverallMolecule➞molecular_weight](OverallMolecule_molecular_weight.md)  <sub>0..1</sub>
     * Description: Molecular weight in Da
     * Range: [QuantityValue](QuantityValue.md)
 * [OverallMolecule➞assembly](OverallMolecule_assembly.md)  <sub>0..1</sub>
     * Description: What type of higher order structure your sample forms - if any.
     * Range: [AssemblyEnum](AssemblyEnum.md)
