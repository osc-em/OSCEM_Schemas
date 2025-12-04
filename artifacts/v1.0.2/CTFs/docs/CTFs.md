
# Class: CTFs

Class representing Contrast Transfer Function (CTF) metadata

URI: [ctf:CTFs](https://w3id.org/oscem-schemas/latest/ctfsCTFs)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Resolution],[Descriptors],[Defocus],[Descriptors]<descriptors%200..*-++[CTFs&#124;amplitude_contrast:float%20%3F],[Astigmatism]<astigmatism%200..1-++[CTFs],[Resolution]<resolution%200..1-++[CTFs],[Defocus]<defocus%200..1-++[CTFs],[Astigmatism])](https://yuml.me/diagram/nofunky;dir:TB/class/[Resolution],[Descriptors],[Defocus],[Descriptors]<descriptors%200..*-++[CTFs&#124;amplitude_contrast:float%20%3F],[Astigmatism]<astigmatism%200..1-++[CTFs],[Resolution]<resolution%200..1-++[CTFs],[Defocus]<defocus%200..1-++[CTFs],[Astigmatism])

## Referenced by Class


## Attributes


### Own

 * [CTFs➞amplitude_contrast](CTFs_amplitude_contrast.md)  <sub>0..1</sub>
     * Description: Amplitude contrast
     * Range: [Float](types/Float.md)
 * [CTFs➞defocus](CTFs_defocus.md)  <sub>0..1</sub>
     * Description: Defocus metadata
     * Range: [Defocus](Defocus.md)
 * [CTFs➞resolution](CTFs_resolution.md)  <sub>0..1</sub>
     * Description: Resolution metadata
     * Range: [Resolution](Resolution.md)
 * [CTFs➞astigmatism](CTFs_astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism metadata
     * Range: [Astigmatism](Astigmatism.md)
 * [CTFs➞descriptors](CTFs_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
