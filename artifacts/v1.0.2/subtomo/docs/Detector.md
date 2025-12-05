
# Class: Detector

Class representing a detector

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-subtomo/Detector](https://w3id.org/oscem-schemas/latest/oscem-schemas-subtomo/Detector)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Range],[QuantitySI],[Range]<collection_angle%200..1-++[Detector&#124;name:string%20%3F;mode:string%20%3F],[QuantitySI]<dispersion%200..1-++[Detector],[Acquisition]++-%20detectors%201..*>[Detector],[Acquisition]++-%20detectors(i)%200..*>[Detector],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Range],[QuantitySI],[Range]<collection_angle%200..1-++[Detector&#124;name:string%20%3F;mode:string%20%3F],[QuantitySI]<dispersion%200..1-++[Detector],[Acquisition]++-%20detectors%201..*>[Detector],[Acquisition]++-%20detectors(i)%200..*>[Detector],[Acquisition])

## Referenced by Class

 *  **[Acquisition](Acquisition.md)** *[Acquisition➞detectors](Acquisition_detectors.md)*  <sub>1..\*</sub>  **[Detector](Detector.md)**
 *  **None** *[detectors](detectors.md)*  <sub>0..\*</sub>  **[Detector](Detector.md)**

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name of the item
     * Range: [String](types/String.md)
 * [mode](mode.md)  <sub>0..1</sub>
     * Description: Mode of the detector, e.g. "counting", "ScanningDetector", "ImagingDetector", etc.
     * Range: [String](types/String.md)
 * [dispersion](dispersion.md)  <sub>0..1</sub>
     * Description: Dispersion of an analytical detector, in eV
     * Range: [QuantitySI](QuantitySI.md)
 * [collection_angle](collection_angle.md)  <sub>0..1</sub>
     * Description: Collection angle set, min and max values in mrad.
     * Range: [Range](Range.md)
