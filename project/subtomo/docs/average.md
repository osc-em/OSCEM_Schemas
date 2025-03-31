
# Class: Average

A particle averaging experiment.

URI: [https://w3id.org/osc-em/oscem-schemas-subtomo/Average](https://w3id.org/osc-em/oscem-schemas-subtomo/Average)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ParticleMap],[ParticleMap]<particle_maps%200..*-++[Average&#124;name:string%20%3F],[Annotation]<annotations%200..*-++[Average],[Dataset]++-%20averages%200..*>[Average],[Processing]++-%20average%200..1>[Average],[Processing],[Dataset],[Annotation])](https://yuml.me/diagram/nofunky;dir:TB/class/[ParticleMap],[ParticleMap]<particle_maps%200..*-++[Average&#124;name:string%20%3F],[Annotation]<annotations%200..*-++[Average],[Dataset]++-%20averages%200..*>[Average],[Processing]++-%20average%200..1>[Average],[Processing],[Dataset],[Annotation])

## Referenced by Class

 *  **None** *[➞averages](dataset__averages.md)*  <sub>0..\*</sub>  **[Average](Average.md)**
 *  **None** *[➞average](processing__average.md)*  <sub>0..1</sub>  **[Average](Average.md)**

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name of a given entry
     * Range: [String](types/String.md)
 * [annotations](annotations.md)  <sub>0..\*</sub>
     * Description: The annotations
     * Range: [Annotation](Annotation.md)
 * [➞particle_maps](average__particle_maps.md)  <sub>0..\*</sub>
     * Description: The particle maps
     * Range: [ParticleMap](ParticleMap.md)
