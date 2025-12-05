
# Class: Classes3D

Class representing classes 3D metadata

URI: [https://w3id.org/oscem-schemas/latest/spa/Classes3D](https://w3id.org/oscem-schemas/latest/spa/Classes3D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Volume],[QuantityValue],[Processing],[Descriptors],[Descriptors]<descriptors%200..*-++[Classes3D&#124;particles_per_3Dclass:integer%20*;images_classes_3D:string%20%3F],[QuantityValue]<resolution_classes_3D%200..1-++[Classes3D],[Volume]<volume%200..*-++[Classes3D],[Processing]++-%20classes3D%200..1>[Classes3D],[Processing]++-%20classes3D(i)%200..1>[Classes3D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Volume],[QuantityValue],[Processing],[Descriptors],[Descriptors]<descriptors%200..*-++[Classes3D&#124;particles_per_3Dclass:integer%20*;images_classes_3D:string%20%3F],[QuantityValue]<resolution_classes_3D%200..1-++[Classes3D],[Volume]<volume%200..*-++[Classes3D],[Processing]++-%20classes3D%200..1>[Classes3D],[Processing]++-%20classes3D(i)%200..1>[Classes3D])

## Referenced by Class

 *  **[Processing](Processing.md)** *[Processing➞classes3D](Processing_classes3D.md)*  <sub>0..1</sub>  **[Classes3D](Classes3D.md)**
 *  **None** *[classes3D](classes3D.md)*  <sub>0..1</sub>  **[Classes3D](Classes3D.md)**

## Attributes


### Own

 * [Classes3D➞particles_per_3Dclass](Classes3D_particles_per_3Dclass.md)  <sub>0..\*</sub>
     * Description: Number of particles per 3D class
     * Range: [Integer](types/Integer.md)
 * [Classes3D➞images_classes_3D](Classes3D_images_classes_3D.md)  <sub>0..1</sub>
     * Description: Filename of the image containing 3D class images
     * Range: [String](types/String.md)
 * [Classes3D➞volume](Classes3D_volume.md)  <sub>0..\*</sub>
     * Description: Describes volume(s) obtained
     * Range: [Volume](Volume.md)
 * [Classes3D➞resolution_classes_3D](Classes3D_resolution_classes_3D.md)  <sub>0..1</sub>
     * Description: Resolution of volume
     * Range: [QuantityValue](QuantityValue.md)
 * [Classes3D➞descriptors](Classes3D_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
