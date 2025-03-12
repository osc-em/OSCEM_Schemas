
# Class: TiltAngle

The min, max and increment of the tilt angle in a tomography session. Unit is degree.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/TiltAngle](https://w3id.org/osc-em/oscem-schemas-subtomo/TiltAngle)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<increment%201..1-++[TiltAngle],[QuantityValue]<maximal%201..1-++[TiltAngle],[QuantityValue]<minimal%201..1-++[TiltAngle],[AcquisitionTomo]++-%20tilt_angle%201..1>[TiltAngle],[AcquisitionTomo]++-%20tilt_angle(i)%200..1>[TiltAngle],[Series]^-[TiltAngle],[Series],[QuantityValue],[AcquisitionTomo])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<increment%201..1-++[TiltAngle],[QuantityValue]<maximal%201..1-++[TiltAngle],[QuantityValue]<minimal%201..1-++[TiltAngle],[AcquisitionTomo]++-%20tilt_angle%201..1>[TiltAngle],[AcquisitionTomo]++-%20tilt_angle(i)%200..1>[TiltAngle],[Series]^-[TiltAngle],[Series],[QuantityValue],[AcquisitionTomo])

## Parents

 *  is_a: [Series](Series.md) - A series of numbers constructed from min, max, and increment

## Referenced by Class

 *  **[AcquisitionTomo](AcquisitionTomo.md)** *[AcquisitionTomo➞tilt_angle](AcquisitionTomo_tilt_angle.md)*  <sub>1..1</sub>  **[TiltAngle](TiltAngle.md)**
 *  **None** *[tilt_angle](tilt_angle.md)*  <sub>0..1</sub>  **[TiltAngle](TiltAngle.md)**

## Attributes


### Own

 * [TiltAngle➞minimal](TiltAngle_minimal.md)  <sub>1..1</sub>
     * Description: Minimal value of a given dataset property
     * Range: [QuantityValue](QuantityValue.md)
 * [TiltAngle➞maximal](TiltAngle_maximal.md)  <sub>1..1</sub>
     * Description: Maximal value of a given dataset property
     * Range: [QuantityValue](QuantityValue.md)
 * [TiltAngle➞increment](TiltAngle_increment.md)  <sub>1..1</sub>
     * Description: Increment between elements of a series
     * Range: [QuantityValue](QuantityValue.md)
