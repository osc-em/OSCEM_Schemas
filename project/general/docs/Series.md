
# Class: Series

A series of numbers constructed from min, max, and increment

URI: [https://w3id.org/osc-em/oscem-schemas-general/Series](https://w3id.org/osc-em/oscem-schemas-general/Series)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Any]<increment%200..1-++[Series],[Range]^-[Series],[Range],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Any]<increment%200..1-++[Series],[Range]^-[Series],[Range],[Any])

## Parents

 *  is_a: [Range](Range.md) - A range constructed from min and max

## Attributes


### Own

 * [increment](increment.md)  <sub>0..1</sub>
     * Description: Increment between elements of a series
     * Range: [Any](Any.md)

### Inherited from Range:

 * [minimal](minimal.md)  <sub>0..1</sub>
     * Description: Minimal value of a given dataset property
     * Range: [Any](Any.md)
 * [maximal](maximal.md)  <sub>0..1</sub>
     * Description: Maximal value of a given dataset property
     * Range: [Any](Any.md)
