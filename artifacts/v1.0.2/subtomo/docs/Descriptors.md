
# Class: Descriptors



URI: [https://w3id.org/oscem-schemas/latest/subtomo/Descriptors](https://w3id.org/oscem-schemas/latest/subtomo/Descriptors)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptor]^-[Descriptors&#124;descriptor_name(i):string],[Descriptor],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptor]^-[Descriptors&#124;descriptor_name(i):string],[Descriptor],[Any])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information

## Referenced by Class

 *  **None** *[descriptors](descriptors.md)*  <sub>0..\*</sub>  **[Descriptors](Descriptors.md)**

## Attributes


### Inherited from Descriptor:

 * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)  <sub>1..1</sub>
     * Description: Name defining the descriptor
     * Range: [String](types/String.md)
 * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)  <sub>0..1</sub>
     * Description: Description of the descriptor
     * Range: [Any](Any.md)
