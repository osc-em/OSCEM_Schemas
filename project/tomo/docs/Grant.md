
# Class: Grant

Grant

URI: [https://w3id.org/osc-em/oscem-schemas-tomo/Grant](https://w3id.org/osc-em/oscem-schemas-tomo/Grant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<budget%200..1-++[Grant&#124;grant_name:string%20%3F;project_id:string%20%3F;country:string%20%3F],[Any]<end_date%200..1-++[Grant],[Any]<start_date%200..1-++[Grant],[Organizational]++-%20grants%200..*>[Grant],[Organizational],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<budget%200..1-++[Grant&#124;grant_name:string%20%3F;project_id:string%20%3F;country:string%20%3F],[Any]<end_date%200..1-++[Grant],[Any]<start_date%200..1-++[Grant],[Organizational]++-%20grants%200..*>[Grant],[Organizational],[Any])

## Referenced by Class

 *  **None** *[grants](grants.md)*  <sub>0..\*</sub>  **[Grant](Grant.md)**

## Attributes


### Own

 * [grant_name](grant_name.md)  <sub>0..1</sub>
     * Description: name of the grant
     * Range: [String](types/String.md)
 * [start_date](start_date.md)  <sub>0..1</sub>
     * Description: start date
     * Range: [Any](Any.md)
 * [end_date](end_date.md)  <sub>0..1</sub>
     * Description: end date
     * Range: [Any](Any.md)
 * [budget](budget.md)  <sub>0..1</sub>
     * Description: budget
     * Range: [QuantityValue](QuantityValue.md)
 * [project_id](project_id.md)  <sub>0..1</sub>
     * Description: project id
     * Range: [String](types/String.md)
 * [country](country.md)  <sub>0..1</sub>
     * Description: Country of the institution
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Grant |