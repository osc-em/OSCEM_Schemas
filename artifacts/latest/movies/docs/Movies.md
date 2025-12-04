
# Class: Movies

Class representing movies metadata

URI: [movies:Movies](https://w3id.org/oscem-schemas/latest/moviesMovies)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Descriptors]<descriptors%200..*-++[Movies&#124;gain_image:string%20%3F;dark_image:string%20%3F],[QuantityValue]<initial_dose%200..1-++[Movies],[QuantityValue]<dose_per_image%200..1-++[Movies],[Descriptors])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Descriptors]<descriptors%200..*-++[Movies&#124;gain_image:string%20%3F;dark_image:string%20%3F],[QuantityValue]<initial_dose%200..1-++[Movies],[QuantityValue]<dose_per_image%200..1-++[Movies],[Descriptors])

## Referenced by Class


## Attributes


### Own

 * [Movies➞dose_per_image](Movies_dose_per_image.md)  <sub>0..1</sub>
     * Description: Dose per image
     * Range: [QuantityValue](QuantityValue.md)
 * [Movies➞initial_dose](Movies_initial_dose.md)  <sub>0..1</sub>
     * Description: Initial dose
     * Range: [QuantityValue](QuantityValue.md)
 * [Movies➞gain_image](Movies_gain_image.md)  <sub>0..1</sub>
     * Description: Gain image filename
     * Range: [String](types/String.md)
 * [Movies➞dark_image](Movies_dark_image.md)  <sub>0..1</sub>
     * Description: Dark image filename
     * Range: [String](types/String.md)
 * [Movies➞descriptors](Movies_descriptors.md)  <sub>0..\*</sub>
     * Description: List of custom descriptors for user-defined key-value pairs describing how movies were obtained or any related information
     * Range: [Descriptors](Descriptors.md)
