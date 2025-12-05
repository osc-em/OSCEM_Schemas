
# Class: QuantityValue

if a value has a unit, it should be given as a unit value pair.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/QuantityValue](https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/QuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Resolution],[Classes2D]++-%20resolution_classes_2D%200..1>[QuantityValue&#124;unit:string;value:float],[Classes3D]++-%20resolution_classes_3D%200..1>[QuantityValue],[Defocus]++-%20output_avg_defocus%200..1>[QuantityValue],[Defocus]++-%20output_max_defocus%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus%200..1>[QuantityValue],[Movies]++-%20dose_per_image%200..1>[QuantityValue],[Movies]++-%20initial_dose%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution%200..1>[QuantityValue],[Volumes]++-%20vol_resolution%200..1>[QuantityValue],[Grant]++-%20budget%200..1>[QuantityValue],[Movies]++-%20dose_per_image(i)%200..1>[QuantityValue],[Movies]++-%20initial_dose(i)%200..1>[QuantityValue],[Defocus]++-%20output_avg_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_max_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution(i)%200..1>[QuantityValue],[Classes2D]++-%20resolution_classes_2D(i)%200..1>[QuantityValue],[Classes3D]++-%20resolution_classes_3D(i)%200..1>[QuantityValue],[Volumes]++-%20vol_resolution(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Movies],[Grant],[Defocus],[Classes3D],[Classes2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Resolution],[Classes2D]++-%20resolution_classes_2D%200..1>[QuantityValue&#124;unit:string;value:float],[Classes3D]++-%20resolution_classes_3D%200..1>[QuantityValue],[Defocus]++-%20output_avg_defocus%200..1>[QuantityValue],[Defocus]++-%20output_max_defocus%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus%200..1>[QuantityValue],[Movies]++-%20dose_per_image%200..1>[QuantityValue],[Movies]++-%20initial_dose%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution%200..1>[QuantityValue],[Volumes]++-%20vol_resolution%200..1>[QuantityValue],[Grant]++-%20budget%200..1>[QuantityValue],[Movies]++-%20dose_per_image(i)%200..1>[QuantityValue],[Movies]++-%20initial_dose(i)%200..1>[QuantityValue],[Defocus]++-%20output_avg_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_avg_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_max_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_max_resolution(i)%200..1>[QuantityValue],[Defocus]++-%20output_min_defocus(i)%200..1>[QuantityValue],[Resolution]++-%20output_min_resolution(i)%200..1>[QuantityValue],[Classes2D]++-%20resolution_classes_2D(i)%200..1>[QuantityValue],[Classes3D]++-%20resolution_classes_3D(i)%200..1>[QuantityValue],[Volumes]++-%20vol_resolution(i)%200..1>[QuantityValue],[QuantityValue]^-[QuantitySI],[QuantitySI],[Movies],[Grant],[Defocus],[Classes3D],[Classes2D])

## Children

 * [QuantitySI](QuantitySI.md) - unit value extended to have two additional fields si_value and si_unit

## Referenced by Class

 *  **[Classes2D](Classes2D.md)** *[Classes2D➞resolution_classes_2D](Classes2D_resolution_classes_2D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Classes3D](Classes3D.md)** *[Classes3D➞resolution_classes_3D](Classes3D_resolution_classes_3D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Defocus](Defocus.md)** *[Defocus➞output_avg_defocus](Defocus_output_avg_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Defocus](Defocus.md)** *[Defocus➞output_max_defocus](Defocus_output_max_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Defocus](Defocus.md)** *[Defocus➞output_min_defocus](Defocus_output_min_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Movies](Movies.md)** *[Movies➞dose_per_image](Movies_dose_per_image.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Movies](Movies.md)** *[Movies➞initial_dose](Movies_initial_dose.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Resolution](Resolution.md)** *[Resolution➞output_avg_resolution](Resolution_output_avg_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Resolution](Resolution.md)** *[Resolution➞output_max_resolution](Resolution_output_max_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Resolution](Resolution.md)** *[Resolution➞output_min_resolution](Resolution_output_min_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[Volumes](Volumes.md)** *[Volumes➞vol_resolution](Volumes_vol_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[budget](budget.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[dose_per_image](dose_per_image.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[initial_dose](initial_dose.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_avg_defocus](output_avg_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_avg_resolution](output_avg_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_max_defocus](output_max_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_max_resolution](output_max_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_min_defocus](output_min_defocus.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[output_min_resolution](output_min_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[resolution_classes_2D](resolution_classes_2D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[resolution_classes_3D](resolution_classes_3D.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[vol_resolution](vol_resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**

## Attributes


### Own

 * [QuantityValue➞unit](QuantityValue_unit.md)  <sub>1..1</sub>
     * Description: the unit of a given value
     * Range: [String](types/String.md)
 * [QuantityValue➞value](QuantityValue_value.md)  <sub>1..1</sub>
     * Description: the value of a field with a unit
     * Range: [Float](types/Float.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | qudt:quantityValue |
