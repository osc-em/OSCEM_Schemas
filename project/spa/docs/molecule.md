
# Class: Molecule

More detailed information about individual molecules.

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Molecule](https://w3id.org/osc-em/oscem-schemas-spa/Molecule)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Sample]++-%20molecule%200..*>[Molecule&#124;name_mol:string;molecular_type:string%20%3F;molecular_class:string%20%3F;sequence:string;natural_source:string;taxonomy_id_source:string%20%3F;expression_system:string%20%3F;taxonomy_id_expression:string%20%3F;gene_name:string%20%3F],[Sample]++-%20molecule(i)%200..*>[Molecule])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Sample]++-%20molecule%200..*>[Molecule&#124;name_mol:string;molecular_type:string%20%3F;molecular_class:string%20%3F;sequence:string;natural_source:string;taxonomy_id_source:string%20%3F;expression_system:string%20%3F;taxonomy_id_expression:string%20%3F;gene_name:string%20%3F],[Sample]++-%20molecule(i)%200..*>[Molecule])

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞molecule](Sample_molecule.md)*  <sub>0..\*</sub>  **[Molecule](Molecule.md)**
 *  **None** *[molecule](molecule.md)*  <sub>0..\*</sub>  **[Molecule](Molecule.md)**

## Attributes


### Own

 * [Molecule➞name_mol](Molecule_name_mol.md)  <sub>1..1</sub>
     * Description: Name of an individual molecule (often protein) in the sample
     * Range: [String](types/String.md)
 * [Molecule➞molecular_type](Molecule_molecular_type.md)  <sub>0..1</sub>
     * Description: Description of the overall molecular type, i.e., a complex
     * Range: [String](types/String.md)
 * [Molecule➞molecular_class](Molecule_molecular_class.md)  <sub>0..1</sub>
     * Description: Class of the molecule
     * Range: [String](types/String.md)
 * [Molecule➞sequence](Molecule_sequence.md)  <sub>1..1</sub>
     * Description: Full sequence of the sample as in the data, i.e., cleaved tags should also be removed from sequence here
     * Range: [String](types/String.md)
 * [Molecule➞natural_source](Molecule_natural_source.md)  <sub>1..1</sub>
     * Description: Scientific name of the natural host organism
     * Range: [String](types/String.md)
 * [Molecule➞taxonomy_id_source](Molecule_taxonomy_id_source.md)  <sub>0..1</sub>
     * Description: Taxonomy ID of the natural source organism
     * Range: [String](types/String.md)
 * [Molecule➞expression_system](Molecule_expression_system.md)  <sub>0..1</sub>
     * Description: Scientific name of the organism used to produce the molecule of interest
     * Range: [String](types/String.md)
 * [Molecule➞taxonomy_id_expression](Molecule_taxonomy_id_expression.md)  <sub>0..1</sub>
     * Description: Taxonomy ID of the expression system organism
     * Range: [String](types/String.md)
 * [Molecule➞gene_name](Molecule_gene_name.md)  <sub>0..1</sub>
     * Description: Name of the gene of interest
     * Range: [String](types/String.md)
