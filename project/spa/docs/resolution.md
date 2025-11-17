
# Class: Resolution

Resolution-related metadata

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Resolution](https://w3id.org/osc-em/oscem-schemas-spa/Resolution)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<output_avg_resolution%200..1-++[Resolution&#124;resolution_histogram:string%20%3F],[QuantityValue]<output_max_resolution%200..1-++[Resolution],[QuantityValue]<output_min_resolution%200..1-++[Resolution],[CTFs]++-%20resolution%200..1>[Resolution],[CTFs]++-%20resolution(i)%200..1>[Resolution],[QuantityValue],[CTFs])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<output_avg_resolution%200..1-++[Resolution&#124;resolution_histogram:string%20%3F],[QuantityValue]<output_max_resolution%200..1-++[Resolution],[QuantityValue]<output_min_resolution%200..1-++[Resolution],[CTFs]++-%20resolution%200..1>[Resolution],[CTFs]++-%20resolution(i)%200..1>[Resolution],[QuantityValue],[CTFs])

## Referenced by Class

 *  **[CTFs](CTFs.md)** *[CTFs➞resolution](CTFs_resolution.md)*  <sub>0..1</sub>  **[Resolution](Resolution.md)**
 *  **None** *[resolution](resolution.md)*  <sub>0..1</sub>  **[Resolution](Resolution.md)**

## Attributes


### Own

 * [Resolution➞output_min_resolution](Resolution_output_min_resolution.md)  <sub>0..1</sub>
     * Description: Minimum resolution
     * Range: [QuantityValue](QuantityValue.md)
 * [Resolution➞output_max_resolution](Resolution_output_max_resolution.md)  <sub>0..1</sub>
     * Description: Maximum resolution
     * Range: [QuantityValue](QuantityValue.md)
 * [Resolution➞output_avg_resolution](Resolution_output_avg_resolution.md)  <sub>0..1</sub>
     * Description: Average value of resolution
     * Range: [QuantityValue](QuantityValue.md)
 * [Resolution➞resolution_histogram](Resolution_resolution_histogram.md)  <sub>0..1</sub>
     * Description: Filename of the resolution values histogram
     * Range: [String](types/String.md)
