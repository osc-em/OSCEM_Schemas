
# Class: Thinning

how the frozen sample was thinned by i.e. FiB-milling

URI: [sample_env:Thinning](https://w3id.org/oscem-schemas/latest/environmental_sampleThinning)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI]<target_thickness%200..1-++[Thinning&#124;method_thin:string%20%3F;instrument_thin:string%20%3F;ion_source:string%20%3F;lift_out:boolean%20%3F],[SampleEnv]++-%20thinning%200..1>[Thinning],[SampleEnv],[QuantitySI])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI]<target_thickness%200..1-++[Thinning&#124;method_thin:string%20%3F;instrument_thin:string%20%3F;ion_source:string%20%3F;lift_out:boolean%20%3F],[SampleEnv]++-%20thinning%200..1>[Thinning],[SampleEnv],[QuantitySI])

## Referenced by Class

 *  **None** *[thinning](thinning.md)*  <sub>0..1</sub>  **[Thinning](Thinning.md)**

## Attributes


### Own

 * [method_thin](method_thin.md)  <sub>0..1</sub>
     * Description: The thinning method used, such as FIB milling.
     * Range: [String](types/String.md)
 * [instrument_thin](instrument_thin.md)  <sub>0..1</sub>
     * Description: Instrument used for thinning the sample
     * Range: [String](types/String.md)
 * [ion_source](ion_source.md)  <sub>0..1</sub>
     * Description: what ion source was used?
     * Range: [String](types/String.md)
 * [target_thickness](target_thickness.md)  <sub>0..1</sub>
     * Description: What was the target thickness of the lamella; in nm.
     * Range: [QuantitySI](QuantitySI.md)
 * [lift_out](lift_out.md)  <sub>0..1</sub>
     * Description: whether a lift out was performed
     * Range: [Boolean](types/Boolean.md)
