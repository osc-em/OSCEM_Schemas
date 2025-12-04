
# Class: SphericalAberrationCorrector

Special device used to correct instrument inherent spherical aberration.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/SphericalAberrationCorrector](https://w3id.org/oscem-schemas/latest/oscem-schemas-cellular-tomo/SphericalAberrationCorrector)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialistOptics]++-%20spherical_aberration_corrector%200..1>[SphericalAberrationCorrector&#124;used:boolean;instrument_type:string],[SpecialistOptics])](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialistOptics]++-%20spherical_aberration_corrector%200..1>[SphericalAberrationCorrector&#124;used:boolean;instrument_type:string],[SpecialistOptics])

## Referenced by Class

 *  **None** *[spherical_aberration_corrector](spherical_aberration_corrector.md)*  <sub>0..1</sub>  **[SphericalAberrationCorrector](SphericalAberrationCorrector.md)**

## Attributes


### Own

 * [SphericalAberrationCorrector➞used](SphericalAberrationCorrector_used.md)  <sub>1..1</sub>
     * Description: whether a specific instrument was used during data acquisition
     * Range: [Boolean](types/Boolean.md)
 * [SphericalAberrationCorrector➞instrument_type](SphericalAberrationCorrector_instrument_type.md)  <sub>1..1</sub>
     * Description: Details of a given specialist instrument
     * Range: [String](types/String.md)
