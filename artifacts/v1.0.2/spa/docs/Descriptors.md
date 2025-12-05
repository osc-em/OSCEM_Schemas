
# Class: Descriptors



URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/Descriptors](https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/Descriptors)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Movies],[Micrographs],[CTFs]++-%20descriptors%200..*>[Descriptors&#124;descriptor_name(i):string],[Classes2D]++-%20descriptors%200..*>[Descriptors],[Classes3D]++-%20descriptors%200..*>[Descriptors],[Coordinates]++-%20descriptors%200..*>[Descriptors],[Micrographs]++-%20descriptors%200..*>[Descriptors],[Movies]++-%20descriptors%200..*>[Descriptors],[Volumes]++-%20descriptors%200..*>[Descriptors],[Movies]++-%20descriptors(i)%200..*>[Descriptors],[Micrographs]++-%20descriptors(i)%200..*>[Descriptors],[CTFs]++-%20descriptors(i)%200..*>[Descriptors],[Coordinates]++-%20descriptors(i)%200..*>[Descriptors],[Classes2D]++-%20descriptors(i)%200..*>[Descriptors],[Classes3D]++-%20descriptors(i)%200..*>[Descriptors],[Volumes]++-%20descriptors(i)%200..*>[Descriptors],[Descriptor]^-[Descriptors],[Descriptor],[Coordinates],[Classes3D],[Classes2D],[CTFs],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Movies],[Micrographs],[CTFs]++-%20descriptors%200..*>[Descriptors&#124;descriptor_name(i):string],[Classes2D]++-%20descriptors%200..*>[Descriptors],[Classes3D]++-%20descriptors%200..*>[Descriptors],[Coordinates]++-%20descriptors%200..*>[Descriptors],[Micrographs]++-%20descriptors%200..*>[Descriptors],[Movies]++-%20descriptors%200..*>[Descriptors],[Volumes]++-%20descriptors%200..*>[Descriptors],[Movies]++-%20descriptors(i)%200..*>[Descriptors],[Micrographs]++-%20descriptors(i)%200..*>[Descriptors],[CTFs]++-%20descriptors(i)%200..*>[Descriptors],[Coordinates]++-%20descriptors(i)%200..*>[Descriptors],[Classes2D]++-%20descriptors(i)%200..*>[Descriptors],[Classes3D]++-%20descriptors(i)%200..*>[Descriptors],[Volumes]++-%20descriptors(i)%200..*>[Descriptors],[Descriptor]^-[Descriptors],[Descriptor],[Coordinates],[Classes3D],[Classes2D],[CTFs],[Any])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information

## Referenced by Class

 *  **[CTFs](CTFs.md)** *[CTFs➞descriptors](CTFs_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **[Classes2D](Classes2D.md)** *[Classes2D➞descriptors](Classes2D_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **[Classes3D](Classes3D.md)** *[Classes3D➞descriptors](Classes3D_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **[Coordinates](Coordinates.md)** *[Coordinates➞descriptors](Coordinates_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **[Micrographs](Micrographs.md)** *[Micrographs➞descriptors](Micrographs_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **[Movies](Movies.md)** *[Movies➞descriptors](Movies_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **[Volumes](Volumes.md)** *[Volumes➞descriptors](Volumes_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **None** *[descriptors](descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**

## Attributes


### Inherited from Descriptor:

 * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)  <sub>1..1</sub>
     * Description: Name defining the descriptor
     * Range: [String](types/String.md)
 * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)  <sub>0..1</sub>
     * Description: Description of the descriptor
     * Range: [Any](Any.md)
