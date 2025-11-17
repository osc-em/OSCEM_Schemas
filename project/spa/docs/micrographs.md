
# Class: Micrographs

Class representing micrographs metadata

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Micrographs](https://w3id.org/osc-em/oscem-schemas-spa/Micrographs)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Processing],[Descriptors]<descriptors%200..*-++[Micrographs&#124;number_micrographs:float],[Processing]++-%20micrographs%200..1>[Micrographs],[Processing]++-%20micrographs(i)%200..1>[Micrographs],[Descriptors])](https://yuml.me/diagram/nofunky;dir:TB/class/[Processing],[Descriptors]<descriptors%200..*-++[Micrographs&#124;number_micrographs:float],[Processing]++-%20micrographs%200..1>[Micrographs],[Processing]++-%20micrographs(i)%200..1>[Micrographs],[Descriptors])

## Referenced by Class

 *  **[Processing](Processing.md)** *[Processing➞micrographs](Processing_micrographs.md)*  <sub>0..1</sub>  **[Micrographs](Micrographs.md)**
 *  **None** *[micrographs](micrographs.md)*  <sub>0..1</sub>  **[Micrographs](Micrographs.md)**

## Attributes


### Own

 * [Micrographs➞number_micrographs](Micrographs_number_micrographs.md)  <sub>1..1</sub>
     * Description: Number of micrographs
     * Range: [Float](types/Float.md)
 * [Micrographs➞descriptors](Micrographs_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
