
# Class: Series

A series of numbers constructed from min, max, and increment

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Series](https://w3id.org/osc-em/oscem-schemas-spa/Series)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI]<increment%200..1-++[Series],[Range]^-[Series],[Range],[QuantitySI])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI]<increment%200..1-++[Series],[Range]^-[Series],[Range],[QuantitySI])

## Parents

 *  is_a: [Range](Range.md) - A range constructed from min and max

## Attributes


### Own

 * [increment](increment.md)  <sub>0..1</sub>
     * Description: Increment between elements of a series
     * Range: [QuantitySI](QuantitySI.md)

### Inherited from Range:

 * [minimal](minimal.md)  <sub>0..1</sub>
     * Description: Minimal value of a given dataset property
     * Range: [QuantitySI](QuantitySI.md)
 * [maximal](maximal.md)  <sub>0..1</sub>
     * Description: Maximal value of a given dataset property
     * Range: [QuantitySI](QuantitySI.md)
