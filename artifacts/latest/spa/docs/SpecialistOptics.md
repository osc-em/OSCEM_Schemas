
# Class: SpecialistOptics

Optional optics used to correct for instrument limitations.

URI: [https://w3id.org/oscem-schemas/latest/spa/SpecialistOptics](https://w3id.org/oscem-schemas/latest/spa/SpecialistOptics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SphericalAberrationCorrector],[ChromaticAberrationCorrector]<chromatic_aberration_corrector%200..1-++[SpecialistOptics],[SphericalAberrationCorrector]<spherical_aberration_corrector%200..1-++[SpecialistOptics],[Phaseplate]<phaseplate%200..1-++[SpecialistOptics],[Acquisition]++-%20specialist_optics%200..1>[SpecialistOptics],[Phaseplate],[ChromaticAberrationCorrector],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[SphericalAberrationCorrector],[ChromaticAberrationCorrector]<chromatic_aberration_corrector%200..1-++[SpecialistOptics],[SphericalAberrationCorrector]<spherical_aberration_corrector%200..1-++[SpecialistOptics],[Phaseplate]<phaseplate%200..1-++[SpecialistOptics],[Acquisition]++-%20specialist_optics%200..1>[SpecialistOptics],[Phaseplate],[ChromaticAberrationCorrector],[Acquisition])

## Referenced by Class

 *  **None** *[specialist_optics](specialist_optics.md)*  <sub>0..1</sub>  **[SpecialistOptics](SpecialistOptics.md)**

## Attributes


### Own

 * [phaseplate](phaseplate.md)  <sub>0..1</sub>
     * Description: Phaseplate is a special optics device that can be used to enhance contrast
     * Range: [Phaseplate](Phaseplate.md)
 * [spherical_aberration_corrector](spherical_aberration_corrector.md)  <sub>0..1</sub>
     * Description: Specialist device to correct for spherical aberration of the microscope lenses
     * Range: [SphericalAberrationCorrector](SphericalAberrationCorrector.md)
 * [chromatic_aberration_corrector](chromatic_aberration_corrector.md)  <sub>0..1</sub>
     * Description: Specialist device to correct for chromatic aberration of the microscope lenses
     * Range: [ChromaticAberrationCorrector](ChromaticAberrationCorrector.md)
