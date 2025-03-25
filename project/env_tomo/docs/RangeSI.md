
# Class: RangeSI

A range constructed from min and max, si units attached

URI: [https://w3id.org/osc-em/oscem-schemas-env-tomo/RangeSI](https://w3id.org/osc-em/oscem-schemas-env-tomo/RangeSI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI]<maximal_si%200..1-++[RangeSI],[QuantitySI]<minimal_si%200..1-++[RangeSI],[Acquisition]++-%20calibrated_defocus%200..1>[RangeSI],[Acquisition]++-%20nominal_defocus%200..1>[RangeSI],[Acquisition]++-%20temperature%200..1>[RangeSI],[QuantitySI],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI]<maximal_si%200..1-++[RangeSI],[QuantitySI]<minimal_si%200..1-++[RangeSI],[Acquisition]++-%20calibrated_defocus%200..1>[RangeSI],[Acquisition]++-%20nominal_defocus%200..1>[RangeSI],[Acquisition]++-%20temperature%200..1>[RangeSI],[QuantitySI],[Acquisition])

## Referenced by Class

 *  **None** *[calibrated_defocus](calibrated_defocus.md)*  <sub>0..1</sub>  **[RangeSI](RangeSI.md)**
 *  **None** *[nominal_defocus](nominal_defocus.md)*  <sub>0..1</sub>  **[RangeSI](RangeSI.md)**
 *  **None** *[➞temperature](temperature_range.md)*  <sub>0..1</sub>  **[RangeSI](RangeSI.md)**

## Attributes


### Own

 * [minimal_si](minimal_si.md)  <sub>0..1</sub>
     * Description: Minimal value of a given dataset property, with si units
     * Range: [QuantitySI](QuantitySI.md)
 * [maximal_si](maximal_si.md)  <sub>0..1</sub>
     * Description: Maximal value of a given dataset property, with si units
     * Range: [QuantitySI](QuantitySI.md)
