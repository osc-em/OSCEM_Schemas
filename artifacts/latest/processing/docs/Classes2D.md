
# Class: Classes2D

Class representing classes 2D metadata

URI: [processing:Classes2D](https://w3id.org/oscem-schemas/latest/processingClasses2D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Processing],[Descriptors],[Descriptors]<descriptors%200..*-++[Classes2D&#124;particles_per_2Dclass:integer%20*;images_classes_2D:string%20%3F],[QuantityValue]<resolution_classes_2D%200..1-++[Classes2D],[Processing]++-%20classes2D%200..1>[Classes2D],[Processing]++-%20classes2D(i)%200..1>[Classes2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Processing],[Descriptors],[Descriptors]<descriptors%200..*-++[Classes2D&#124;particles_per_2Dclass:integer%20*;images_classes_2D:string%20%3F],[QuantityValue]<resolution_classes_2D%200..1-++[Classes2D],[Processing]++-%20classes2D%200..1>[Classes2D],[Processing]++-%20classes2D(i)%200..1>[Classes2D])

## Referenced by Class

 *  **[Processing](Processing.md)** *[Processing➞classes2D](Processing_classes2D.md)*  <sub>0..1</sub>  **[Classes2D](Classes2D.md)**
 *  **None** *[classes2D](classes2D.md)*  <sub>0..1</sub>  **[Classes2D](Classes2D.md)**

## Attributes


### Own

 * [Classes2D➞particles_per_2Dclass](Classes2D_particles_per_2Dclass.md)  <sub>0..\*</sub>
     * Description: Number of particles per 2D class
     * Range: [Integer](types/Integer.md)
 * [Classes2D➞images_classes_2D](Classes2D_images_classes_2D.md)  <sub>0..1</sub>
     * Description: Filename of the image containing 2D class images
     * Range: [String](types/String.md)
 * [Classes2D➞resolution_classes_2D](Classes2D_resolution_classes_2D.md)  <sub>0..1</sub>
     * Description: Resolution of classes 2D
     * Range: [QuantityValue](QuantityValue.md)
 * [Classes2D➞descriptors](Classes2D_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
