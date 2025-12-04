
# Class: EnergyFilter

A device used to filter for electrons with specific energy.

URI: [https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/EnergyFilter](https://w3id.org/oscem-schemas/latest/oscem-schemas-spa/EnergyFilter)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<width_energy_filter%201..1-++[EnergyFilter&#124;used:boolean;model:string%20%3F],[Acquisition]++-%20energy_filter%200..1>[EnergyFilter],[Acquisition])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantitySI],[QuantitySI]<width_energy_filter%201..1-++[EnergyFilter&#124;used:boolean;model:string%20%3F],[Acquisition]++-%20energy_filter%200..1>[EnergyFilter],[Acquisition])

## Referenced by Class

 *  **None** *[energy_filter](energy_filter.md)*  <sub>0..1</sub>  **[EnergyFilter](EnergyFilter.md)**

## Attributes


### Own

 * [EnergyFilter➞used](EnergyFilter_used.md)  <sub>1..1</sub>
     * Description: whether a specific instrument was used during data acquisition
     * Range: [Boolean](types/Boolean.md)
 * [EnergyFilter➞model](EnergyFilter_model.md)  <sub>0..1</sub>
     * Description: The model of the item
     * Range: [String](types/String.md)
 * [EnergyFilter➞width_energy_filter](EnergyFilter_width_energy_filter.md)  <sub>1..1</sub>
     * Description: Width of the energy filter used.
     * Range: [QuantitySI](QuantitySI.md)
