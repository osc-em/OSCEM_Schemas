
# Class: ImageSize

size of a 2D image (in integer units)

URI: [https://w3id.org/osc-em/oscem-schemas-spa/ImageSize](https://w3id.org/osc-em/oscem-schemas-spa/ImageSize)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Acquisition]++-%20binning_camera%201..1>[ImageSize&#124;height:integer%20%3F;width:integer%20%3F],[Acquisition]++-%20binning_camera(i)%200..1>[ImageSize],[Acquisition]++-%20image_size%200..1>[ImageSize],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Acquisition]++-%20binning_camera%201..1>[ImageSize&#124;height:integer%20%3F;width:integer%20%3F],[Acquisition]++-%20binning_camera(i)%200..1>[ImageSize],[Acquisition]++-%20image_size%200..1>[ImageSize],[Acquisition])

## Referenced by Class

 *  **[Acquisition](Acquisition.md)** *[Acquisition➞binning_camera](Acquisition_binning_camera.md)*  <sub>1..1</sub>  **[ImageSize](ImageSize.md)**
 *  **None** *[binning_camera](binning_camera.md)*  <sub>0..1</sub>  **[ImageSize](ImageSize.md)**
 *  **None** *[image_size](image_size.md)*  <sub>0..1</sub>  **[ImageSize](ImageSize.md)**

## Attributes


### Own

 * [height](height.md)  <sub>0..1</sub>
     * Description: The height of a given item - unit depends on item
     * Range: [Integer](types/Integer.md)
 * [width](width.md)  <sub>0..1</sub>
     * Description: The width of a given item - unit depends on item
     * Range: [Integer](types/Integer.md)
