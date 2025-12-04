
# Class: Descriptors



URI: [micrographs:Descriptors](https://w3id.org/oscem-schemas/latest/micrographsDescriptors)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Micrographs],[Micrographs]++-%20descriptors%200..*>[Descriptors&#124;descriptor_name(i):string],[Micrographs]++-%20descriptors(i)%200..*>[Descriptors],[Descriptor]^-[Descriptors],[Descriptor],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Micrographs],[Micrographs]++-%20descriptors%200..*>[Descriptors&#124;descriptor_name(i):string],[Micrographs]++-%20descriptors(i)%200..*>[Descriptors],[Descriptor]^-[Descriptors],[Descriptor],[Any])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information

## Referenced by Class

 *  **[Micrographs](Micrographs.md)** *[Micrographs➞descriptors](Micrographs_descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**
 *  **None** *[descriptors](descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**

## Attributes


### Inherited from Descriptor:

 * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)  <sub>1..1</sub>
     * Description: Name defining the descriptor
     * Range: [String](types/String.md)
 * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)  <sub>0..1</sub>
     * Description: Description of the descriptor
     * Range: [Any](Any.md)
