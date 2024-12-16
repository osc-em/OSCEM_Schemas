
# Class: Organizational

Overarching category for authors and grants

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Organizational](https://w3id.org/osc-em/oscem-schemas-spa/Organizational)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Funder]<funder%201..*-++[Organizational],[Author]<authors%201..*-++[Organizational],[Grant]<grants%200..*-++[Organizational],[EMDatasetSpa]++-%20organizational%200..1>[Organizational],[Grant],[Funder],[EMDatasetSpa],[Author])](https://yuml.me/diagram/nofunky;dir:TB/class/[Funder]<funder%201..*-++[Organizational],[Author]<authors%201..*-++[Organizational],[Grant]<grants%200..*-++[Organizational],[EMDatasetSpa]++-%20organizational%200..1>[Organizational],[Grant],[Funder],[EMDatasetSpa],[Author])

## Referenced by Class

 *  **[EMDatasetSpa](EMDatasetSpa.md)** *[EMDatasetSpa➞organizational](EMDatasetSpa_organizational.md)*  <sub>0..1</sub>  **[Organizational](Organizational.md)**

## Attributes


### Own

 * [grants](grants.md)  <sub>0..\*</sub>
     * Description: List of grants associated with the project
     * Range: [Grant](Grant.md)
 * [Organizational➞authors](Organizational_authors.md)  <sub>1..\*</sub>
     * Description: List of authors associated with the project
     * Range: [Author](Author.md)
 * [Organizational➞funder](Organizational_funder.md)  <sub>1..\*</sub>
     * Description: funding organization/person.
     * Range: [Funder](Funder.md)
