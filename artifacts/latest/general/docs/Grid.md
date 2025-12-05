
# Class: Grid

Details on the grid used in the experiment.

URI: [https://w3id.org/oscem-schemas/latest/general/Grid](https://w3id.org/oscem-schemas/latest/general/Grid)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[QuantitySI],[QuantitySI]<pretreatment_pressure%200..1-++[Grid&#124;manufacturer:string%20%3F;material:string%20%3F;mesh:float%20%3F;film_support:boolean%20%3F;film_material:string%20%3F;film_topology:string%20%3F;film_thickness:string%20%3F;pretreatment_type:string%20%3F;pretreatment_atmosphere:string%20%3F],[QuantitySI]<pretreatment_time%200..1-++[Grid],[Sample]++-%20grid%200..1>[Grid],[Sample]++-%20grid(i)%200..1>[Grid])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[QuantitySI],[QuantitySI]<pretreatment_pressure%200..1-++[Grid&#124;manufacturer:string%20%3F;material:string%20%3F;mesh:float%20%3F;film_support:boolean%20%3F;film_material:string%20%3F;film_topology:string%20%3F;film_thickness:string%20%3F;pretreatment_type:string%20%3F;pretreatment_atmosphere:string%20%3F],[QuantitySI]<pretreatment_time%200..1-++[Grid],[Sample]++-%20grid%200..1>[Grid],[Sample]++-%20grid(i)%200..1>[Grid])

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞grid](Sample_grid.md)*  <sub>0..1</sub>  **[Grid](Grid.md)**
 *  **None** *[grid](grid.md)*  <sub>0..1</sub>  **[Grid](Grid.md)**

## Attributes


### Own

 * [Grid➞manufacturer](Grid_manufacturer.md)  <sub>0..1</sub>
     * Description: The name of the manufacturer
     * Range: [String](types/String.md)
 * [Grid➞material](Grid_material.md)  <sub>0..1</sub>
     * Description: Material out of which the grid is made
     * Range: [String](types/String.md)
 * [Grid➞mesh](Grid_mesh.md)  <sub>0..1</sub>
     * Description: Grid mesh in lines per inch
     * Range: [Float](types/Float.md)
 * [Grid➞film_support](Grid_film_support.md)  <sub>0..1</sub>
     * Description: Whether a support film was used
     * Range: [Boolean](types/Boolean.md)
 * [Grid➞film_material](Grid_film_material.md)  <sub>0..1</sub>
     * Description: Type of material the support film is made of
     * Range: [String](types/String.md)
 * [Grid➞film_topology](Grid_film_topology.md)  <sub>0..1</sub>
     * Description: Topology of the support film
     * Range: [String](types/String.md)
 * [Grid➞film_thickness](Grid_film_thickness.md)  <sub>0..1</sub>
     * Description: Thickness of the support film
     * Range: [String](types/String.md)
 * [Grid➞pretreatment_type](Grid_pretreatment_type.md)  <sub>0..1</sub>
     * Description: Type of pretreatment of the grid, i.e., glow discharge
     * Range: [String](types/String.md)
 * [Grid➞pretreatment_time](Grid_pretreatment_time.md)  <sub>0..1</sub>
     * Description: Length of time of the pretreatment in s
     * Range: [QuantitySI](QuantitySI.md)
 * [Grid➞pretreatment_pressure](Grid_pretreatment_pressure.md)  <sub>0..1</sub>
     * Description: Pressure of the chamber during pretreatment, in Pa
     * Range: [QuantitySI](QuantitySI.md)
 * [Grid➞pretreatment_atmosphere](Grid_pretreatment_atmosphere.md)  <sub>0..1</sub>
     * Description: Atmospheric conditions in the chamber during pretreatment, i.e., addition of specific gases, etc.
     * Range: [String](types/String.md)
