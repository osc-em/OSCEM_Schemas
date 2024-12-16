
# Class: SampleCell

Unifying class to describe the full sample with growth conditions

URI: [https://w3id.org/osc-em/oscem-schemas-cellular-tomo/SampleCell](https://w3id.org/osc-em/oscem-schemas-cellular-tomo/SampleCell)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[SampleEnv],[GrowthCondition]<growth_condition%200..1-++[SampleCell],[EMDatasetCell]++-%20sample%200..1>[SampleCell],[SampleEnv]^-[SampleCell],[GrowthCondition],[Freezing],[EMDatasetCell])](https://yuml.me/diagram/nofunky;dir:TB/class/[TomogramFeatures],[Thinning],[SpecimenEnv],[SampleEnv],[GrowthCondition]<growth_condition%200..1-++[SampleCell],[EMDatasetCell]++-%20sample%200..1>[SampleCell],[SampleEnv]^-[SampleCell],[GrowthCondition],[Freezing],[EMDatasetCell])

## Parents

 *  is_a: [SampleEnv](SampleEnv.md) - Unifying class to describe the full sample.

## Referenced by Class

 *  **[EMDatasetCell](EMDatasetCell.md)** *[EMDatasetCell➞sample](EMDatasetCell_sample.md)*  <sub>0..1</sub>  **[SampleCell](SampleCell.md)**

## Attributes


### Own

 * [growth_condition](growth_condition.md)  <sub>0..1</sub>
     * Description: how the specimen was grown
     * Range: [GrowthCondition](GrowthCondition.md)

### Inherited from SampleEnv:

 * [specimen_env](specimen_env.md)  <sub>0..1</sub>
     * Range: [SpecimenEnv](SpecimenEnv.md)
 * [freezing](freezing.md)  <sub>0..1</sub>
     * Range: [Freezing](Freezing.md)
 * [thinning](thinning.md)  <sub>0..1</sub>
     * Range: [Thinning](Thinning.md)
 * [tomogram_features](tomogram_features.md)  <sub>0..1</sub>
     * Range: [TomogramFeatures](TomogramFeatures.md)
