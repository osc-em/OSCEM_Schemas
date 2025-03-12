
# Class: Defocus

Defocus-related metadata

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Defocus](https://w3id.org/osc-em/oscem-schemas-spa/Defocus)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<output_avg_defocus%200..1-++[Defocus&#124;defocus_histogram:string%20%3F;defocus_micrograph_examples:string%20%3F],[QuantityValue]<output_max_defocus%200..1-++[Defocus],[QuantityValue]<output_min_defocus%200..1-++[Defocus],[CTFs]++-%20defocus%200..1>[Defocus],[CTFs]++-%20defocus(i)%200..1>[Defocus],[CTFs])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<output_avg_defocus%200..1-++[Defocus&#124;defocus_histogram:string%20%3F;defocus_micrograph_examples:string%20%3F],[QuantityValue]<output_max_defocus%200..1-++[Defocus],[QuantityValue]<output_min_defocus%200..1-++[Defocus],[CTFs]++-%20defocus%200..1>[Defocus],[CTFs]++-%20defocus(i)%200..1>[Defocus],[CTFs])

## Referenced by Class

 *  **[CTFs](CTFs.md)** *[CTFs➞defocus](CTFs_defocus.md)*  <sub>0..1</sub>  **[Defocus](Defocus.md)**
 *  **None** *[defocus](defocus.md)*  <sub>0..1</sub>  **[Defocus](Defocus.md)**

## Attributes


### Own

 * [Defocus➞output_min_defocus](Defocus_output_min_defocus.md)  <sub>0..1</sub>
     * Description: Minimum defocus
     * Range: [QuantityValue](QuantityValue.md)
 * [Defocus➞output_max_defocus](Defocus_output_max_defocus.md)  <sub>0..1</sub>
     * Description: Maximum defocus
     * Range: [QuantityValue](QuantityValue.md)
 * [Defocus➞output_avg_defocus](Defocus_output_avg_defocus.md)  <sub>0..1</sub>
     * Description: Average value of defocus
     * Range: [QuantityValue](QuantityValue.md)
 * [Defocus➞defocus_histogram](Defocus_defocus_histogram.md)  <sub>0..1</sub>
     * Description: Filename of the defocus values histogram
     * Range: [String](types/String.md)
 * [Defocus➞defocus_micrograph_examples](Defocus_defocus_micrograph_examples.md)  <sub>0..1</sub>
     * Description: Filename of micrographs shown as examples in ascending order of defocus value
     * Range: [String](types/String.md)
