
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [acquisition:QuantitySI](https://w3id.org/oscem-schemas/latest/acquisitionQuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Acquisition]++-%20pixel_size%201..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[EnergyFilter]++-%20width_energy_filter%201..1>[QuantitySI],[Detector]++-%20dispersion%200..1>[QuantitySI],[Acquisition]++-%20dose_per_movie%200..1>[QuantitySI],[Acquisition]++-%20exposure_time%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[Acquisition]++-%20pixel_size(i)%200..1>[QuantitySI],[Acquisition]++-%20screen_current%200..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[EnergyFilter],[Detector],[BoundingBox2D],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Acquisition]++-%20pixel_size%201..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[EnergyFilter]++-%20width_energy_filter%201..1>[QuantitySI],[Detector]++-%20dispersion%200..1>[QuantitySI],[Acquisition]++-%20dose_per_movie%200..1>[QuantitySI],[Acquisition]++-%20exposure_time%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[Acquisition]++-%20pixel_size(i)%200..1>[QuantitySI],[Acquisition]++-%20screen_current%200..1>[QuantitySI],[EnergyFilter]++-%20width_energy_filter(i)%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[EnergyFilter],[Detector],[BoundingBox2D],[Acquisition])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class

 *  **[Acquisition](Acquisition.md)** *[Acquisition➞pixel_size](Acquisition_pixel_size.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[EnergyFilter](EnergyFilter.md)** *[EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[dispersion](dispersion.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[dose_per_movie](dose_per_movie.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[exposure_time](exposure_time.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[pixel_size](pixel_size.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[screen_current](screen_current.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[width_energy_filter](width_energy_filter.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[x_max](x_max.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[x_min](x_min.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[y_max](y_max.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[y_min](y_min.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**

## Attributes


### Own

 * [valueSI](valueSI.md)  <sub>0..1</sub>
     * Description: value of a given field in respect to its SI unit
     * Range: [Float](types/Float.md)
 * [unitSI](unitSI.md)  <sub>0..1</sub>
     * Description: the SI unit attached to a si value
     * Range: [String](types/String.md)

### Inherited from QuantityValue:

 * [QuantityValue➞unit](QuantityValue_unit.md)  <sub>1..1</sub>
     * Description: the unit of a given value
     * Range: [String](types/String.md)
 * [QuantityValue➞value](QuantityValue_value.md)  <sub>1..1</sub>
     * Description: the value of a field with a unit
     * Range: [Float](types/Float.md)
