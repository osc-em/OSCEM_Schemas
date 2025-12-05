
# Class: Author

Details on the person performing the experiment.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/Author](https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/Author)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[Organizational],[Organizational]++-%20authors%201..*>[Author&#124;orcid:string%20%3F;country:string%20%3F;role:string%20%3F;name_org:string%20%3F;type_org:OrganizationTypeEnum;family_name:string;given_name:string;email:string;job_title(i):boolean%20%3F;telephone(i):string%20%3F],[Organizational]++-%20authors(i)%200..*>[Author],[Person]^-[Author])](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[Organizational],[Organizational]++-%20authors%201..*>[Author&#124;orcid:string%20%3F;country:string%20%3F;role:string%20%3F;name_org:string%20%3F;type_org:OrganizationTypeEnum;family_name:string;given_name:string;email:string;job_title(i):boolean%20%3F;telephone(i):string%20%3F],[Organizational]++-%20authors(i)%200..*>[Author],[Person]^-[Author])

## Parents

 *  is_a: [Person](Person.md) - personal information

## Referenced by Class

 *  **[Organizational](Organizational.md)** *[Organizational➞authors](Organizational_authors.md)*  <sub>1..\*</sub>  **[Author](Author.md)**
 *  **None** *[authors](authors.md)*  <sub>0..\*</sub>  **[Author](Author.md)**

## Attributes


### Own

 * [Author➞orcid](Author_orcid.md)  <sub>0..1</sub>
     * Description: ORCID of the author, a type of unique identifier
     * Range: [String](types/String.md)
 * [Author➞country](Author_country.md)  <sub>0..1</sub>
     * Description: Country of the institution
     * Range: [String](types/String.md)
 * [role](role.md)  <sub>0..1</sub>
     * Description: Role of the author, for example principal investigator
     * Range: [String](types/String.md)
 * [Author➞name_org](Author_name_org.md)  <sub>0..1</sub>
     * Description: Name of the organization
     * Range: [String](types/String.md)
 * [Author➞type_org](Author_type_org.md)  <sub>1..1</sub>
     * Description: Type of organization, academic, commercial, governmental, etc.
     * Range: [OrganizationTypeEnum](OrganizationTypeEnum.md)
 * [Author➞family_name](Author_family_name.md)  <sub>1..1</sub>
     * Description: last name
     * Range: [String](types/String.md)
 * [Author➞given_name](Author_given_name.md)  <sub>1..1</sub>
     * Description: first name
     * Range: [String](types/String.md)
 * [Author➞email](Author_email.md)  <sub>1..1</sub>
     * Description: email
     * Range: [String](types/String.md)

### Inherited from Person:

 * [job_title](job_title.md)  <sub>0..1</sub>
     * Description: job title
     * Range: [Boolean](types/Boolean.md)
 * [telephone](telephone.md)  <sub>0..1</sub>
     * Description: work phone
     * Range: [String](types/String.md)
