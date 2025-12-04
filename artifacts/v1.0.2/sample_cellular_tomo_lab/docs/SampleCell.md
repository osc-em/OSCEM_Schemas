
# Class: SampleCell

Unifying class to describe the full sample with growth conditions

URI: [cellular_tomo:SampleCell](https://w3id.org/oscem-schemas/latest/cellular_tomoSampleCell)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[SampleEnv],[GrowthCondition]<growth_condition%200..1-++[SampleCell],[SampleEnv]^-[SampleCell],[GrowthCondition],[Freezing])](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[SampleEnv],[GrowthCondition]<growth_condition%200..1-++[SampleCell],[SampleEnv]^-[SampleCell],[GrowthCondition],[Freezing])

## Parents

 *  is_a: [SampleEnv](SampleEnv.md) - Unifying class to describe the full sample.

## Attributes


### Own

 * [growth_condition](growth_condition.md)  <sub>0..1</sub>
     * Description: How the specimen was grown
     * Range: [GrowthCondition](GrowthCondition.md)

### Inherited from SampleEnv:

 * [SampleEnv➞specimen_env](SampleEnv_specimen_env.md)  <sub>1..1</sub>
     * Range: [SpecimenEnv](SpecimenEnv.md)
 * [freezing](freezing.md)  <sub>0..1</sub>
     * Range: [Freezing](Freezing.md)
 * [thinning](thinning.md)  <sub>0..1</sub>
     * Range: [Thinning](Thinning.md)
 * [tomogram_features](tomogram_features.md)  <sub>0..1</sub>
     * Range: [TomogramFeatures](TomogramFeatures.md)
