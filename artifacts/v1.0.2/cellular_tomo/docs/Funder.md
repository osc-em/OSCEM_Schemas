
# Class: Funder

Description of the project funding

URI: [https://w3id.org/oscem-schemas/latest/cellular_tomo/Funder](https://w3id.org/oscem-schemas/latest/cellular_tomo/Funder)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organizational],[Organizational]++-%20funder%200..*>[Funder&#124;funder_name:string%20%3F;type_org:OrganizationTypeEnum%20%3F;country:string%20%3F],[Organizational]++-%20funder(i)%200..*>[Funder])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organizational],[Organizational]++-%20funder%200..*>[Funder&#124;funder_name:string%20%3F;type_org:OrganizationTypeEnum%20%3F;country:string%20%3F],[Organizational]++-%20funder(i)%200..*>[Funder])

## Referenced by Class

 *  **[Organizational](Organizational.md)** *[Organizational➞funder](Organizational_funder.md)*  <sub>0..\*</sub>  **[Funder](Funder.md)**
 *  **None** *[funder](funder.md)*  <sub>0..\*</sub>  **[Funder](Funder.md)**

## Attributes


### Own

 * [funder_name](funder_name.md)  <sub>0..1</sub>
     * Description: funding organization/person.
     * Range: [String](types/String.md)
 * [type_org](type_org.md)  <sub>0..1</sub>
     * Description: Type of organization, academic, commercial, governmental, etc.
     * Range: [OrganizationTypeEnum](OrganizationTypeEnum.md)
 * [country](country.md)  <sub>0..1</sub>
     * Description: Country of the institution
     * Range: [String](types/String.md)
