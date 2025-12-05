
# Class: GrowthCondition

How the cells were grown

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/GrowthCondition](https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/GrowthCondition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<temperature_growth%200..1-++[GrowthCondition&#124;media:string%20%3F;growth_location:string%20%3F;cell_cycle:string%20%3F;treatment:string%20%3F;atmosphere_growth:string%20%3F],[SampleCell]++-%20growth_condition%200..1>[GrowthCondition],[SampleCell])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<temperature_growth%200..1-++[GrowthCondition&#124;media:string%20%3F;growth_location:string%20%3F;cell_cycle:string%20%3F;treatment:string%20%3F;atmosphere_growth:string%20%3F],[SampleCell]++-%20growth_condition%200..1>[GrowthCondition],[SampleCell])

## Referenced by Class

 *  **None** *[growth_condition](growth_condition.md)*  <sub>0..1</sub>  **[GrowthCondition](GrowthCondition.md)**

## Attributes


### Own

 * [media](media.md)  <sub>0..1</sub>
     * Description: What growth media was used
     * Range: [String](types/String.md)
 * [growth_location](growth_location.md)  <sub>0..1</sub>
     * Description: In/on what kind of surface/container the cells were grown; i.e. directly on a grid
     * Range: [String](types/String.md)
 * [cell_cycle](cell_cycle.md)  <sub>0..1</sub>
     * Description: What was the targeted cell cycle state, if any
     * Range: [String](types/String.md)
 * [treatment](treatment.md)  <sub>0..1</sub>
     * Description: Were there any special treatment conditions; such as addition of certain chemicals etc
     * Range: [String](types/String.md)
 * [atmosphere_growth](atmosphere_growth.md)  <sub>0..1</sub>
     * Description: What was the atmosphere the sample was in, elaborate on any special gases present etc.
     * Range: [String](types/String.md)
 * [temperature_growth](temperature_growth.md)  <sub>0..1</sub>
     * Description: Temperature of the sample; in K.
     * Range: [QuantitySI](QuantitySI.md)
