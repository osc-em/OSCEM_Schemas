
# Class: Range

A range constructed from min and max

URI: [https://w3id.org/osc-em/oscem-schemas-env-tomo/Range](https://w3id.org/osc-em/oscem-schemas-env-tomo/Range)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Series],[Any]<maximal%200..1-++[Range],[Any]<minimal%200..1-++[Range],[Acquisition]++-%20calibrated_defocus%200..1>[Range],[Acquisition]++-%20nominal_defocus%200..1>[Range],[Acquisition]++-%20temperature%200..1>[Range],[Range]^-[Series],[Any],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Series],[Any]<maximal%200..1-++[Range],[Any]<minimal%200..1-++[Range],[Acquisition]++-%20calibrated_defocus%200..1>[Range],[Acquisition]++-%20nominal_defocus%200..1>[Range],[Acquisition]++-%20temperature%200..1>[Range],[Range]^-[Series],[Any],[Acquisition])

## Children

 * [Series](Series.md) - A series of numbers constructed from min, max, and increment

## Referenced by Class

 *  **None** *[calibrated_defocus](calibrated_defocus.md)*  <sub>0..1</sub>  **[Range](Range.md)**
 *  **None** *[nominal_defocus](nominal_defocus.md)*  <sub>0..1</sub>  **[Range](Range.md)**
 *  **None** *[➞temperature](temperature_range.md)*  <sub>0..1</sub>  **[Range](Range.md)**

## Attributes


### Own

 * [minimal](minimal.md)  <sub>0..1</sub>
     * Description: Minimal value of a given dataset property
     * Range: [Any](Any.md)
 * [maximal](maximal.md)  <sub>0..1</sub>
     * Description: Maximal value of a given dataset property
     * Range: [Any](Any.md)
