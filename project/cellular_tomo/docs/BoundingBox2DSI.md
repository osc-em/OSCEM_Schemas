
# Class: BoundingBox2DSI

an axis-aligned 2D bounding box (float units) with SI unit attached

URI: [https://w3id.org/osc-em/oscem-schemas-cellular-tomo/BoundingBox2DSI](https://w3id.org/osc-em/oscem-schemas-cellular-tomo/BoundingBox2DSI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<y_max_si%200..1-++[BoundingBox2DSI],[QuantitySI]<y_min_si%200..1-++[BoundingBox2DSI],[QuantitySI]<x_max_si%200..1-++[BoundingBox2DSI],[QuantitySI]<x_min_si%200..1-++[BoundingBox2DSI],[Acquisition]++-%20imageshift%200..1>[BoundingBox2DSI],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<y_max_si%200..1-++[BoundingBox2DSI],[QuantitySI]<y_min_si%200..1-++[BoundingBox2DSI],[QuantitySI]<x_max_si%200..1-++[BoundingBox2DSI],[QuantitySI]<x_min_si%200..1-++[BoundingBox2DSI],[Acquisition]++-%20imageshift%200..1>[BoundingBox2DSI],[Acquisition])

## Referenced by Class

 *  **None** *[imageshift](imageshift.md)*  <sub>0..1</sub>  **[BoundingBox2DSI](BoundingBox2DSI.md)**

## Attributes


### Own

 * [x_min_si](x_min_si.md)  <sub>0..1</sub>
     * Description: minimum x, with si units
     * Range: [QuantitySI](QuantitySI.md)
 * [x_max_si](x_max_si.md)  <sub>0..1</sub>
     * Description: maximum x, with si units
     * Range: [QuantitySI](QuantitySI.md)
 * [y_min_si](y_min_si.md)  <sub>0..1</sub>
     * Description: minimum y, with si units
     * Range: [QuantitySI](QuantitySI.md)
 * [y_max_si](y_max_si.md)  <sub>0..1</sub>
     * Description: maximum y, with si units
     * Range: [QuantitySI](QuantitySI.md)
