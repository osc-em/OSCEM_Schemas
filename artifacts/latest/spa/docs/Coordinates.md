
# Class: Coordinates

Class representing coordinates metadata

URI: [https://w3id.org/oscem-schemas/latest/spa/Coordinates](https://w3id.org/oscem-schemas/latest/spa/Coordinates)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Processing],[Descriptors],[Descriptors]<descriptors%200..*-++[Coordinates&#124;number_particles:integer;particles_per_micrograph:float%20%3F;num_source_micrographs:integer%20%3F;particles_histogram:string%20%3F;micrograph_examples:string%20%3F],[Processing]++-%20coordinates%200..1>[Coordinates],[Processing]++-%20coordinates(i)%200..1>[Coordinates])](https://yuml.me/diagram/nofunky;dir:TB/class/[Processing],[Descriptors],[Descriptors]<descriptors%200..*-++[Coordinates&#124;number_particles:integer;particles_per_micrograph:float%20%3F;num_source_micrographs:integer%20%3F;particles_histogram:string%20%3F;micrograph_examples:string%20%3F],[Processing]++-%20coordinates%200..1>[Coordinates],[Processing]++-%20coordinates(i)%200..1>[Coordinates])

## Referenced by Class

 *  **[Processing](Processing.md)** *[Processing➞coordinates](Processing_coordinates.md)*  <sub>0..1</sub>  **[Coordinates](Coordinates.md)**
 *  **None** *[coordinates](coordinates.md)*  <sub>0..1</sub>  **[Coordinates](Coordinates.md)**

## Attributes


### Own

 * [Coordinates➞number_particles](Coordinates_number_particles.md)  <sub>1..1</sub>
     * Description: Total number of particles
     * Range: [Integer](types/Integer.md)
 * [Coordinates➞particles_per_micrograph](Coordinates_particles_per_micrograph.md)  <sub>0..1</sub>
     * Description: Mean number of particles per micrograph
     * Range: [Float](types/Float.md)
 * [Coordinates➞num_source_micrographs](Coordinates_num_source_micrographs.md)  <sub>0..1</sub>
     * Description: Total number of micrographs from which coordinates come from
     * Range: [Integer](types/Integer.md)
 * [Coordinates➞particles_histogram](Coordinates_particles_histogram.md)  <sub>0..1</sub>
     * Description: Filename of histogram for particle number per micrograph
     * Range: [String](types/String.md)
 * [Coordinates➞micrograph_examples](Coordinates_micrograph_examples.md)  <sub>0..1</sub>
     * Description: Filename of micrographs shown as examples in descending order based on the number of particles
     * Range: [String](types/String.md)
 * [Coordinates➞descriptors](Coordinates_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
