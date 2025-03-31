
# Class: Dataset

A dataset

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Dataset](https://w3id.org/osc-em/oscem-schemas-subtomo/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Region],[Average]<averages%200..*-++[Dataset&#124;name:string%20%3F],[Region]<regions%200..*-++[Dataset],[Processing]++-%20dataset%200..1>[Dataset],[Processing],[Average])](https://yuml.me/diagram/nofunky;dir:TB/class/[Region],[Average]<averages%200..*-++[Dataset&#124;name:string%20%3F],[Region]<regions%200..*-++[Dataset],[Processing]++-%20dataset%200..1>[Dataset],[Processing],[Average])

## Referenced by Class

 *  **None** *[➞dataset](processing__dataset.md)*  <sub>0..1</sub>  **[Dataset](Dataset.md)**

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name of a given entry
     * Range: [String](types/String.md)
 * [➞regions](dataset__regions.md)  <sub>0..\*</sub>
     * Description: The regions in the dataset
     * Range: [Region](Region.md)
 * [➞averages](dataset__averages.md)  <sub>0..\*</sub>
     * Description: The averages in the dataset
     * Range: [Average](Average.md)
