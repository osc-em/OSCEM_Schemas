
# Class: Specimen

Description of specimen handling.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Specimen](https://w3id.org/osc-em/oscem-schemas-subtomo/Specimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<temperature%200..1-++[Specimen&#124;buffer:string%20%3F;ph:float%20%3F;vitrification:boolean%20%3F;vitrification_cryogen:string%20%3F;staining:boolean%20%3F;embedding:boolean%20%3F;shadowing:boolean%20%3F],[QuantityValue]<humidity%200..1-++[Specimen],[QuantityValue]<concentration%200..1-++[Specimen],[Sample]++-%20specimen%200..1>[Specimen],[Sample]++-%20specimen(i)%200..1>[Specimen],[Sample],[QuantityValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<temperature%200..1-++[Specimen&#124;buffer:string%20%3F;ph:float%20%3F;vitrification:boolean%20%3F;vitrification_cryogen:string%20%3F;staining:boolean%20%3F;embedding:boolean%20%3F;shadowing:boolean%20%3F],[QuantityValue]<humidity%200..1-++[Specimen],[QuantityValue]<concentration%200..1-++[Specimen],[Sample]++-%20specimen%200..1>[Specimen],[Sample]++-%20specimen(i)%200..1>[Specimen],[Sample],[QuantityValue])

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞specimen](Sample_specimen.md)*  <sub>0..1</sub>  **[Specimen](Specimen.md)**
 *  **None** *[specimen](specimen.md)*  <sub>0..1</sub>  **[Specimen](Specimen.md)**

## Attributes


### Own

 * [Specimen➞buffer](Specimen_buffer.md)  <sub>0..1</sub>
     * Description: Name/composition of the (chemical) sample buffer during grid preparation
     * Range: [String](types/String.md)
 * [Specimen➞concentration](Specimen_concentration.md)  <sub>0..1</sub>
     * Description: Concentration of the (supra)molecule in the sample, in mg/ml
     * Range: [QuantityValue](QuantityValue.md)
 * [Specimen➞ph](Specimen_ph.md)  <sub>0..1</sub>
     * Description: pH of the sample buffer
     * Range: [Float](types/Float.md)
 * [Specimen➞vitrification](Specimen_vitrification.md)  <sub>0..1</sub>
     * Description: Whether the sample was vitrified
     * Range: [Boolean](types/Boolean.md)
 * [Specimen➞vitrification_cryogen](Specimen_vitrification_cryogen.md)  <sub>0..1</sub>
     * Description: Which cryogen was used for vitrification
     * Range: [String](types/String.md)
 * [Specimen➞humidity](Specimen_humidity.md)  <sub>0..1</sub>
     * Description: Environmental humidity just before vitrification, in %
     * Range: [QuantityValue](QuantityValue.md)
 * [Specimen➞temperature](Specimen_temperature.md)  <sub>0..1</sub>
     * Description: Environmental temperature just before vitrification, in K
     * Range: [QuantityValue](QuantityValue.md)
 * [Specimen➞staining](Specimen_staining.md)  <sub>0..1</sub>
     * Description: Whether the sample was stained
     * Range: [Boolean](types/Boolean.md)
 * [Specimen➞embedding](Specimen_embedding.md)  <sub>0..1</sub>
     * Description: Whether the sample was embedded
     * Range: [Boolean](types/Boolean.md)
 * [Specimen➞shadowing](Specimen_shadowing.md)  <sub>0..1</sub>
     * Description: Whether the sample was shadowed
     * Range: [Boolean](types/Boolean.md)
