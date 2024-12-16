
# Class: Series

A series of numbers constructed from min, max, and increment

URI: [https://w3id.org/osc-em/oscem-schemas-spa/Series](https://w3id.org/osc-em/oscem-schemas-spa/Series)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<increment%200..1-++[Series],[Range]^-[Series],[Range],[QuantityValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<increment%200..1-++[Series],[Range]^-[Series],[Range],[QuantityValue])

## Parents

 *  is_a: [Range](Range.md) - A range constructed from min and max

## Attributes


### Own

 * [increment](increment.md)  <sub>0..1</sub>
     * Description: Increment between elements of a series
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from Range:

 * [minimal](minimal.md)  <sub>0..1</sub>
     * Description: Minimal value of a given dataset property
     * Range: [QuantityValue](QuantityValue.md)
 * [maximal](maximal.md)  <sub>0..1</sub>
     * Description: Maximal value of a given dataset property
     * Range: [QuantityValue](QuantityValue.md)
