
# Class: Descriptors



URI: [volumes:Descriptors](https://w3id.org/oscem-schemas/latest/volumesDescriptors)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Classes3D]++-%20descriptors%200..*>[Descriptors&#124;descriptor_name(i):string],[Volumes]++-%20descriptors%200..*>[Descriptors],[Volumes]++-%20descriptors(i)%200..*>[Descriptors],[Classes3D]++-%20descriptors(i)%200..*>[Descriptors],[Descriptor]^-[Descriptors],[Descriptor],[Classes3D],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Classes3D]++-%20descriptors%200..*>[Descriptors&#124;descriptor_name(i):string],[Volumes]++-%20descriptors%200..*>[Descriptors],[Volumes]++-%20descriptors(i)%200..*>[Descriptors],[Classes3D]++-%20descriptors(i)%200..*>[Descriptors],[Descriptor]^-[Descriptors],[Descriptor],[Classes3D],[Any])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information

## Referenced by Class

 *  **[Classes3D](Classes3D.md)** *[Classes3D➞descriptors](Classes3D_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
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
