
# Class: Volumes

Class representing volume metadata

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Volumes](https://w3id.org/osc-em/oscem-schemas-spa/Volumes)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptors]<descriptors%200..*-++[Volumes&#124;volume_type:string;vol_number_particles:integer%20%3F;size:string%20%3F],[QuantityValue]<vol_resolution%200..1-++[Volumes],[IsosurfaceImages]<isosurface_images%200..1-++[Volumes],[OrthogonalSlices]<orthogonal_slices%200..1-++[Volumes],[Processing]++-%20volumes%200..*>[Volumes],[Processing]++-%20volumes(i)%200..*>[Volumes],[QuantityValue],[Processing],[OrthogonalSlices],[IsosurfaceImages],[Descriptors])](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptors]<descriptors%200..*-++[Volumes&#124;volume_type:string;vol_number_particles:integer%20%3F;size:string%20%3F],[QuantityValue]<vol_resolution%200..1-++[Volumes],[IsosurfaceImages]<isosurface_images%200..1-++[Volumes],[OrthogonalSlices]<orthogonal_slices%200..1-++[Volumes],[Processing]++-%20volumes%200..*>[Volumes],[Processing]++-%20volumes(i)%200..*>[Volumes],[QuantityValue],[Processing],[OrthogonalSlices],[IsosurfaceImages],[Descriptors])

## Referenced by Class

 *  **[Processing](Processing.md)** *[Processing➞volumes](Processing_volumes.md)*  <sub>0..\*</sub>  **[Volumes](Volumes.md)**
 *  **None** *[volumes](volumes.md)*  <sub>0..\*</sub>  **[Volumes](Volumes.md)**

## Attributes


### Own

 * [Volumes➞volume_type](Volumes_volume_type.md)  <sub>1..1</sub>
     * Description: Indicates the type of volume
     * Range: [String](types/String.md)
 * [Volumes➞vol_number_particles](Volumes_vol_number_particles.md)  <sub>0..1</sub>
     * Description: Number of particles associated to volume
     * Range: [Integer](types/Integer.md)
 * [Volumes➞size](Volumes_size.md)  <sub>0..1</sub>
     * Description: Size of the volume
     * Range: [String](types/String.md)
 * [Volumes➞orthogonal_slices](Volumes_orthogonal_slices.md)  <sub>0..1</sub>
     * Description: orthogonal slices of volume
     * Range: [OrthogonalSlices](OrthogonalSlices.md)
 * [Volumes➞isosurface_images](Volumes_isosurface_images.md)  <sub>0..1</sub>
     * Description: isosurface images of volume
     * Range: [IsosurfaceImages](IsosurfaceImages.md)
 * [Volumes➞vol_resolution](Volumes_vol_resolution.md)  <sub>0..1</sub>
     * Description: Resolution of volume
     * Range: [QuantityValue](QuantityValue.md)
 * [Volumes➞descriptors](Volumes_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
