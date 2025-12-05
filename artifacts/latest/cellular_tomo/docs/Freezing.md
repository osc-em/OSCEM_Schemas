
# Class: Freezing

how the sample was frozen.

URI: [https://w3id.org/oscem-schemas/latest/cellular_tomo/Freezing](https://w3id.org/oscem-schemas/latest/cellular_tomo/Freezing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<temperature_env%200..1-++[Freezing&#124;cryogen_sample_env:string%20%3F;method:FreezingMethodEnum%20%3F;blotting:boolean%20%3F;atmosphere:string%20%3F;details:string%20%3F],[QuantitySI]<humidity_env%200..1-++[Freezing],[SampleEnv]++-%20freezing%200..1>[Freezing],[SampleEnv])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<temperature_env%200..1-++[Freezing&#124;cryogen_sample_env:string%20%3F;method:FreezingMethodEnum%20%3F;blotting:boolean%20%3F;atmosphere:string%20%3F;details:string%20%3F],[QuantitySI]<humidity_env%200..1-++[Freezing],[SampleEnv]++-%20freezing%200..1>[Freezing],[SampleEnv])

## Referenced by Class

 *  **None** *[freezing](freezing.md)*  <sub>0..1</sub>  **[Freezing](Freezing.md)**

## Attributes


### Own

 * [cryogen_sample_env](cryogen_sample_env.md)  <sub>0..1</sub>
     * Description: the cryogen used to freeze the sample, i.e. ethane
     * Range: [String](types/String.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: freezing method - such as plunge freezing, high pressure freezing etc.
     * Range: [FreezingMethodEnum](FreezingMethodEnum.md)
 * [blotting](blotting.md)  <sub>0..1</sub>
     * Description: whether blotting was performed.
     * Range: [Boolean](types/Boolean.md)
 * [humidity_env](humidity_env.md)  <sub>0..1</sub>
     * Description: humidity of the atmosphere right before/ during freezing; in %.
     * Range: [QuantitySI](QuantitySI.md)
 * [temperature_env](temperature_env.md)  <sub>0..1</sub>
     * Description: temperature of the sample right before freezing; in K.
     * Range: [QuantitySI](QuantitySI.md)
 * [atmosphere](atmosphere.md)  <sub>0..1</sub>
     * Description: What was the atmosphere the sample was in right before freezing, elaborate on any special gases present etc.
     * Range: [String](types/String.md)
 * [details](details.md)  <sub>0..1</sub>
     * Description: Any further comments on the freezing process go here.
     * Range: [String](types/String.md)
