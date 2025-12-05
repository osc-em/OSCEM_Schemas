
# Class: ChromaticAberrationCorrector

Special device used to correct instrument inherent chromatic aberration.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-env-tomo/ChromaticAberrationCorrector](https://w3id.org/oscem-schemas/latest/oscem-schemas-env-tomo/ChromaticAberrationCorrector)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialistOptics]++-%20chromatic_aberration_corrector%200..1>[ChromaticAberrationCorrector&#124;used:boolean;instrument_type:string],[SpecialistOptics])](https://yuml.me/diagram/nofunky;dir:TB/class/[SpecialistOptics]++-%20chromatic_aberration_corrector%200..1>[ChromaticAberrationCorrector&#124;used:boolean;instrument_type:string],[SpecialistOptics])

## Referenced by Class

 *  **None** *[chromatic_aberration_corrector](chromatic_aberration_corrector.md)*  <sub>0..1</sub>  **[ChromaticAberrationCorrector](ChromaticAberrationCorrector.md)**

## Attributes


### Own

 * [ChromaticAberrationCorrector➞used](ChromaticAberrationCorrector_used.md)  <sub>1..1</sub>
     * Description: whether a specific instrument was used during data acquisition
     * Range: [Boolean](types/Boolean.md)
 * [ChromaticAberrationCorrector➞instrument_type](ChromaticAberrationCorrector_instrument_type.md)  <sub>1..1</sub>
     * Description: Details of a given specialist instrument
     * Range: [String](types/String.md)
