
# Class: Micrographs

Class representing micrographs metadata

URI: [micrographs:Micrographs](https://w3id.org/oscem-schemas/latest/micrographsMicrographs)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptors]<descriptors%200..*-++[Micrographs&#124;number_micrographs:float],[Descriptors])](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptors]<descriptors%200..*-++[Micrographs&#124;number_micrographs:float],[Descriptors])

## Referenced by Class


## Attributes


### Own

 * [Micrographs➞number_micrographs](Micrographs_number_micrographs.md)  <sub>1..1</sub>
     * Description: Number of micrographs
     * Range: [Float](types/Float.md)
 * [Micrographs➞descriptors](Micrographs_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
