
# Class: Range

A range constructed from min and max

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/Range](https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/Range)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Series],[QuantitySI]<maximal%200..1-++[Range],[QuantitySI]<minimal%200..1-++[Range],[Acquisition]++-%20calibrated_defocus%200..1>[Range],[Detector]++-%20collection_angle%200..1>[Range],[Acquisition]++-%20nominal_defocus%200..1>[Range],[Acquisition]++-%20temperature%200..1>[Range],[Range]^-[Series],[QuantitySI],[Detector],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Series],[QuantitySI]<maximal%200..1-++[Range],[QuantitySI]<minimal%200..1-++[Range],[Acquisition]++-%20calibrated_defocus%200..1>[Range],[Detector]++-%20collection_angle%200..1>[Range],[Acquisition]++-%20nominal_defocus%200..1>[Range],[Acquisition]++-%20temperature%200..1>[Range],[Range]^-[Series],[QuantitySI],[Detector],[Acquisition])

## Children

 * [Series](Series.md) - A series of numbers constructed from min, max, and increment

## Referenced by Class

 *  **None** *[calibrated_defocus](calibrated_defocus.md)*  <sub>0..1</sub>  **[Range](Range.md)**
 *  **None** *[collection_angle](collection_angle.md)*  <sub>0..1</sub>  **[Range](Range.md)**
 *  **None** *[nominal_defocus](nominal_defocus.md)*  <sub>0..1</sub>  **[Range](Range.md)**
 *  **None** *[➞temperature](temperature_range.md)*  <sub>0..1</sub>  **[Range](Range.md)**

## Attributes


### Own

 * [minimal](minimal.md)  <sub>0..1</sub>
     * Description: Minimal value of a given dataset property
     * Range: [QuantitySI](QuantitySI.md)
 * [maximal](maximal.md)  <sub>0..1</sub>
     * Description: Maximal value of a given dataset property
     * Range: [QuantitySI](QuantitySI.md)
