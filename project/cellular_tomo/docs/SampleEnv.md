
# Class: SampleEnv

Unifying class to describe the full sample.

URI: [https://w3id.org/osc-em/oscem-schemas-cellular-tomo/SampleEnv](https://w3id.org/osc-em/oscem-schemas-cellular-tomo/SampleEnv)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[TomogramFeatures]<tomogram_features%200..1-++[SampleEnv],[Thinning]<thinning%200..1-++[SampleEnv],[Freezing]<freezing%200..1-++[SampleEnv],[SpecimenEnv]<specimen_env%200..1-++[SampleEnv],[SampleEnv]^-[SampleCell],[SampleCell],[Freezing])](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[TomogramFeatures]<tomogram_features%200..1-++[SampleEnv],[Thinning]<thinning%200..1-++[SampleEnv],[Freezing]<freezing%200..1-++[SampleEnv],[SpecimenEnv]<specimen_env%200..1-++[SampleEnv],[SampleEnv]^-[SampleCell],[SampleCell],[Freezing])

## Children

 * [SampleCell](SampleCell.md) - Unifying class to describe the full sample with growth conditions

## Referenced by Class


## Attributes


### Own

 * [specimen_env](specimen_env.md)  <sub>0..1</sub>
     * Range: [SpecimenEnv](SpecimenEnv.md)
 * [freezing](freezing.md)  <sub>0..1</sub>
     * Range: [Freezing](Freezing.md)
 * [thinning](thinning.md)  <sub>0..1</sub>
     * Range: [Thinning](Thinning.md)
 * [tomogram_features](tomogram_features.md)  <sub>0..1</sub>
     * Range: [TomogramFeatures](TomogramFeatures.md)
