
# Class: SampleEnv

Unifying class to describe the full sample.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-env-tomo/SampleEnv](https://w3id.org/oscem-schemas/latest/oscem-schemas-env-tomo/SampleEnv)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[TomogramFeatures]<tomogram_features%200..1-++[SampleEnv],[Thinning]<thinning%200..1-++[SampleEnv],[Freezing]<freezing%200..1-++[SampleEnv],[SpecimenEnv]<specimen_env%201..1-++[SampleEnv],[EMDatasetEnv]++-%20sample%200..1>[SampleEnv],[Freezing],[EMDatasetEnv])](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[TomogramFeatures]<tomogram_features%200..1-++[SampleEnv],[Thinning]<thinning%200..1-++[SampleEnv],[Freezing]<freezing%200..1-++[SampleEnv],[SpecimenEnv]<specimen_env%201..1-++[SampleEnv],[EMDatasetEnv]++-%20sample%200..1>[SampleEnv],[Freezing],[EMDatasetEnv])

## Referenced by Class

 *  **[EMDatasetEnv](EMDatasetEnv.md)** *[EMDatasetEnv➞sample](EMDatasetEnv_sample.md)*  <sub>0..1</sub>  **[SampleEnv](SampleEnv.md)**

## Attributes


### Own

 * [SampleEnv➞specimen_env](SampleEnv_specimen_env.md)  <sub>1..1</sub>
     * Range: [SpecimenEnv](SpecimenEnv.md)
 * [freezing](freezing.md)  <sub>0..1</sub>
     * Range: [Freezing](Freezing.md)
 * [thinning](thinning.md)  <sub>0..1</sub>
     * Range: [Thinning](Thinning.md)
 * [tomogram_features](tomogram_features.md)  <sub>0..1</sub>
     * Range: [TomogramFeatures](TomogramFeatures.md)
