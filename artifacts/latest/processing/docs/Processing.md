
# Class: Processing

Set of parameters describing the data processing

URI: [processing:Processing](https://w3id.org/oscem-schemas/latest/processingProcessing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Volumes]<volumes%200..*-++[Processing],[Classes3D]<classes3D%200..1-++[Processing],[Classes2D]<classes2D%200..1-++[Processing],[Coordinates]<coordinates%200..1-++[Processing],[CTFs]<ctfs%200..1-++[Processing],[Micrographs]<micrographs%200..1-++[Processing],[Movies]<movies%200..1-++[Processing],[Movies],[Micrographs],[Coordinates],[Classes3D],[Classes2D],[CTFs])](https://yuml.me/diagram/nofunky;dir:TB/class/[Volumes],[Volumes]<volumes%200..*-++[Processing],[Classes3D]<classes3D%200..1-++[Processing],[Classes2D]<classes2D%200..1-++[Processing],[Coordinates]<coordinates%200..1-++[Processing],[CTFs]<ctfs%200..1-++[Processing],[Micrographs]<micrographs%200..1-++[Processing],[Movies]<movies%200..1-++[Processing],[Movies],[Micrographs],[Coordinates],[Classes3D],[Classes2D],[CTFs])

## Referenced by Class


## Attributes


### Own

 * [Processing➞movies](Processing_movies.md)  <sub>0..1</sub>
     * Description: Movies metadata
     * Range: [Movies](Movies.md)
 * [Processing➞micrographs](Processing_micrographs.md)  <sub>0..1</sub>
     * Description: Micrographs metadata
     * Range: [Micrographs](Micrographs.md)
 * [Processing➞ctfs](Processing_ctfs.md)  <sub>0..1</sub>
     * Description: CTFs metadata
     * Range: [CTFs](CTFs.md)
 * [Processing➞coordinates](Processing_coordinates.md)  <sub>0..1</sub>
     * Description: Coordinates metadata
     * Range: [Coordinates](Coordinates.md)
 * [Processing➞classes2D](Processing_classes2D.md)  <sub>0..1</sub>
     * Description: Classes 2D metadata
     * Range: [Classes2D](Classes2D.md)
 * [Processing➞classes3D](Processing_classes3D.md)  <sub>0..1</sub>
     * Description: Classes 3D metadata
     * Range: [Classes3D](Classes3D.md)
 * [Processing➞volumes](Processing_volumes.md)  <sub>0..\*</sub>
     * Description: Volume metadata
     * Range: [Volumes](Volumes.md)
