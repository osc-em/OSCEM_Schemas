
# Class: BoundingBox2D

an axis-aligned 2D bounding box (float units)

URI: [https://w3id.org/osc-em/oscem-schemas-spa/BoundingBox2D](https://w3id.org/osc-em/oscem-schemas-spa/BoundingBox2D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<y_max%200..1-++[BoundingBox2D],[QuantityValue]<y_min%200..1-++[BoundingBox2D],[QuantityValue]<x_max%200..1-++[BoundingBox2D],[QuantityValue]<x_min%200..1-++[BoundingBox2D],[Acquisition]++-%20beamshift%200..1>[BoundingBox2D],[Acquisition]++-%20beamtilt%200..1>[BoundingBox2D],[Acquisition]++-%20imageshift%200..1>[BoundingBox2D],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<y_max%200..1-++[BoundingBox2D],[QuantityValue]<y_min%200..1-++[BoundingBox2D],[QuantityValue]<x_max%200..1-++[BoundingBox2D],[QuantityValue]<x_min%200..1-++[BoundingBox2D],[Acquisition]++-%20beamshift%200..1>[BoundingBox2D],[Acquisition]++-%20beamtilt%200..1>[BoundingBox2D],[Acquisition]++-%20imageshift%200..1>[BoundingBox2D],[Acquisition])

## Referenced by Class

 *  **None** *[beamshift](beamshift.md)*  <sub>0..1</sub>  **[BoundingBox2D](BoundingBox2D.md)**
 *  **None** *[beamtilt](beamtilt.md)*  <sub>0..1</sub>  **[BoundingBox2D](BoundingBox2D.md)**
 *  **None** *[imageshift](imageshift.md)*  <sub>0..1</sub>  **[BoundingBox2D](BoundingBox2D.md)**

## Attributes


### Own

 * [x_min](x_min.md)  <sub>0..1</sub>
     * Description: minimum x
     * Range: [QuantityValue](QuantityValue.md)
 * [x_max](x_max.md)  <sub>0..1</sub>
     * Description: maximum x
     * Range: [QuantityValue](QuantityValue.md)
 * [y_min](y_min.md)  <sub>0..1</sub>
     * Description: minimum y
     * Range: [QuantityValue](QuantityValue.md)
 * [y_max](y_max.md)  <sub>0..1</sub>
     * Description: maximum y
     * Range: [QuantityValue](QuantityValue.md)
