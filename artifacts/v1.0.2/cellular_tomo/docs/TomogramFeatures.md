
# Class: TomogramFeatures

what was the target of the tomograms, and what area of a cell do they cover.

URI: [https://w3id.org/oscem-schemas/latest/cellular_tomo/TomogramFeatures](https://w3id.org/oscem-schemas/latest/cellular_tomo/TomogramFeatures)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleEnv]++-%20tomogram_features%200..1>[TomogramFeatures&#124;cellular_features:string%20%3F;organelles:string%20*;main_target:string%20%3F;details_tomo:string%20%3F],[SampleEnv])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleEnv]++-%20tomogram_features%200..1>[TomogramFeatures&#124;cellular_features:string%20%3F;organelles:string%20*;main_target:string%20%3F;details_tomo:string%20%3F],[SampleEnv])

## Referenced by Class

 *  **None** *[tomogram_features](tomogram_features.md)*  <sub>0..1</sub>  **[TomogramFeatures](TomogramFeatures.md)**

## Attributes


### Own

 * [cellular_features](cellular_features.md)  <sub>0..1</sub>
     * Description: What type of cellular features are present in your tomograms?
     * Range: [String](types/String.md)
 * [organelles](organelles.md)  <sub>0..\*</sub>
     * Description: What organelles; if any; are present?
     * Range: [String](types/String.md)
 * [main_target](main_target.md)  <sub>0..1</sub>
     * Description: What was the main biological target of your research for this tomogram?
     * Range: [String](types/String.md)
 * [details_tomo](details_tomo.md)  <sub>0..1</sub>
     * Description: If you have any further comments on your tomograms please leave them here
     * Range: [String](types/String.md)
