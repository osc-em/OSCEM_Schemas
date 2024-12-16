
# Class: SpecimenEnv

base information on the acquisition and treatment of the sample itself.

URI: [https://w3id.org/osc-em/oscem-schemas-env-tomo/SpecimenEnv](https://w3id.org/osc-em/oscem-schemas-env-tomo/SpecimenEnv)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleEnv]++-%20specimen_env%200..1>[SpecimenEnv&#124;organism:string%20*;tissue:string%20%3F;source_env:string%20%3F;location:string%20%3F;collection_date:date%20%3F;handling:string%20%3F],[SampleEnv])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleEnv]++-%20specimen_env%200..1>[SpecimenEnv&#124;organism:string%20*;tissue:string%20%3F;source_env:string%20%3F;location:string%20%3F;collection_date:date%20%3F;handling:string%20%3F],[SampleEnv])

## Referenced by Class

 *  **None** *[specimen_env](specimen_env.md)*  <sub>0..1</sub>  **[SpecimenEnv](SpecimenEnv.md)**

## Attributes


### Own

 * [organism](organism.md)  <sub>0..\*</sub>
     * Description: the organism(s) present in your sample, if not perfectly defined try to asses as close as possible.
     * Range: [String](types/String.md)
 * [tissue](tissue.md)  <sub>0..1</sub>
     * Description: if the sample is a tissue sample please indicate what type of tissue.
     * Range: [String](types/String.md)
 * [source_env](source_env.md)  <sub>0..1</sub>
     * Description: where is this sample from? i.e. Hospital
     * Range: [String](types/String.md)
 * [location](location.md)  <sub>0..1</sub>
     * Description: the geographical location of your source, optimally in a geographic coordinate system.
     * Range: [String](types/String.md)
 * [collection_date](collection_date.md)  <sub>0..1</sub>
     * Description: When the sample was collected
     * Range: [Date](types/Date.md)
 * [handling](handling.md)  <sub>0..1</sub>
     * Description: What was done to the sample, please give an overview of relevant treatments.
     * Range: [String](types/String.md)
