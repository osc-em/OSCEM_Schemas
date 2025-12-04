
# Class: Descriptor

List of custom descriptors for user-defined key-value pairs describing how micrographs were obtained or any related information

URI: [processing:Descriptor](https://w3id.org/oscem-schemas/latest/processingDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptors],[Any]<descriptor_thing%200..1-++[Descriptor&#124;descriptor_name:string],[Descriptor]^-[Descriptors],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Descriptors],[Any]<descriptor_thing%200..1-++[Descriptor&#124;descriptor_name:string],[Descriptor]^-[Descriptors],[Any])

## Children

 * [Descriptors](Descriptors.md)

## Referenced by Class


## Attributes


### Own

 * [Descriptor➞descriptor_name](Descriptor_descriptor_name.md)  <sub>1..1</sub>
     * Description: Name defining the descriptor
     * Range: [String](types/String.md)
 * [Descriptor➞descriptor_thing](Descriptor_descriptor_thing.md)  <sub>0..1</sub>
     * Description: Description of the descriptor
     * Range: [Any](Any.md)
