
# Class: QuantitySI

unit value extended to have two additional fields si_value and si_unit

URI: [instrument:QuantitySI](https://w3id.org/oscem-schemas/latest/instrumentQuantitySI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Instrument]++-%20acceleration_voltage%201..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Instrument]++-%20beam_convergence%200..1>[QuantitySI],[Instrument]++-%20c2_aperture%200..1>[QuantitySI],[Instrument]++-%20cs%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantitySI],[Instrument]++-%20beam_convergence(i)%200..1>[QuantitySI],[Instrument]++-%20c2_aperture(i)%200..1>[QuantitySI],[Instrument]++-%20cs(i)%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[Instrument],[BoundingBox2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Instrument]++-%20acceleration_voltage%201..1>[QuantitySI&#124;valueSI:float%20%3F;unitSI:string%20%3F;unit(i):string;value(i):float],[Instrument]++-%20beam_convergence%200..1>[QuantitySI],[Instrument]++-%20c2_aperture%200..1>[QuantitySI],[Instrument]++-%20cs%200..1>[QuantitySI],[Instrument]++-%20acceleration_voltage(i)%200..1>[QuantitySI],[Instrument]++-%20beam_convergence(i)%200..1>[QuantitySI],[Instrument]++-%20c2_aperture(i)%200..1>[QuantitySI],[Instrument]++-%20cs(i)%200..1>[QuantitySI],[Series]++-%20increment%200..1>[QuantitySI],[Range]++-%20maximal%200..1>[QuantitySI],[Range]++-%20minimal%200..1>[QuantitySI],[BoundingBox2D]++-%20x_max%200..1>[QuantitySI],[BoundingBox2D]++-%20x_min%200..1>[QuantitySI],[BoundingBox2D]++-%20y_max%200..1>[QuantitySI],[BoundingBox2D]++-%20y_min%200..1>[QuantitySI],[QuantityValue]^-[QuantitySI],[Series],[Range],[Instrument],[BoundingBox2D])

## Parents

 *  is_a: [QuantityValue](QuantityValue.md) - if a value has a unit, it should be given as a unit value pair.

## Referenced by Class

 *  **[Instrument](Instrument.md)** *[Instrument➞acceleration_voltage](Instrument_acceleration_voltage.md)*  <sub>1..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞beam_convergence](Instrument_beam_convergence.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞c2_aperture](Instrument_c2_aperture.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **[Instrument](Instrument.md)** *[Instrument➞cs](Instrument_cs.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[acceleration_voltage](acceleration_voltage.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[beam_convergence](beam_convergence.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[c2_aperture](c2_aperture.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[cs](cs.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[increment](increment.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[maximal](maximal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
 *  **None** *[minimal](minimal.md)*  <sub>0..1</sub>  **[QuantitySI](QuantitySI.md)**
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
