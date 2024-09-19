## EMDataset-001
### Input
```yaml
acquisition:
  binning_camera: 2
  date_time: '2024-01-01'
  detector: Falcon 4i
  detector_mode: counting
  dose_per_movie:
    unit: "e/\u212B\xB2"
    value: 0.5
  holder: testitest
  pixel_size:
    unit: "\u212B"
    value: 1.2
authors:
- country: Switzerland
  email: john.doe@gmail.com
  first_name: John
  name: Doe
  name_org: University of Blub
  orcid: ORCID_123124151231
  type_org: Academic
  work_phone: '+4132112312'
- country: Switzerland
  email: jane.doe@gmail.com
  first_name: Jane
  name: Doe
  name_org: University of Blub
  orcid: ORCID_123124151221
  type_org: Academic
  work_phone: '+4132112312'
grants:
- funder: SNF
  project_id: SNF321
- funder: SNF
  project_id: Fundingofsomekind
instrument:
  acceleration_voltage:
    unit: kV
    value: 300
  c2_aperture:
    unit: "\xB5m"
    value: 70
  cs:
    unit: mm
    value: 2.7
  electron_source: FEG
  illumination: FloodBeam
  imaging: Brightfield
  microscope: Titan
sample:
  grid:
    film_support: false
    manufacturer: Quantifoil
    material: Au
    mesh: 300
    pretreatment_pressure:
      unit: Pa
      value: 1.0e-06
    pretreatment_time:
      unit: s
      value: 30
    pretreatment_type: Glow discharge
  ligands:
  - present: true
    smiles: OCC
  molecule:
  - expression_system: Pichia kudriavzevii
    gene_name: Rib
    molecular_class: None of these
    molecular_type: polypeptide
    name_mol: Ribosome_
    natural_source: yeast
    sequence: MMKNMMKYMMMYSYKEKSEKRRWMMKREMMKYLELLNMRMNKWVKRMMMSRKRLLSRMNRLEKKNHMNDYKLMSYNFNKNSMMMKSMLSKLMMNLLENVMNGVDLKSGKSKMSGGNMMMSKPVMKENLNTVNMLFYYFLPNNKSYKYFNRMNMYLNKHMKNYKKLVKLNKNYSKSSYLLQDKLMMSNMFNNMMFNRNNMKYMNNNVNNLMSSLNMNSNNKSLYLSLLNKTLNNNLSNLYSNNNINKSIINNTLVNMSMLNNNYNNNNTTFNINNNLFNLLNLLNNNYNNNNNYNNMMSNTNMLLNNYNNNNNNNNNNKCNMHSKMKLERKNMMLNYLLKNEMMNKNQMWMSKMENNKMNNINNNNNMLKMNKENDKTNMFGYMMSYMDMLLGNMMNKSKKSNDMKMMMSKYFGLKEVNMTGMNLKYEFNNTEMLLKLMRKGMSKRKRTLSRMFRFRLKNRMPLLNDKGMLKNKMSNNLLKNLALNNNILNVEYNIKNVLFNSINNNNINNNNNNNMYNDMKDYYNNMSLENKKDLSLNNELLYKNMVGWSLLLKGKVGARKGKNRSNRMLMTKGSFKNNNLYIYNIFDDNSNNNGYTKDRLRLNYMKNSNFISYMDKSTNNGKLGMTLKVNIL
    taxonomy_id_expression: GCA_003054445.1
    taxonomy_id_source: GCA_003054445.1
  overall_molecule:
    molecular_type: Complex
    molecular_weight:
      unit: Da
      value: 3000000
    name_sample: Ribosome
    source: yeast
  specimen:
    concentration:
      unit: M
      value: 0.3
    embedding: false
    humidity:
      unit: '%'
      value: 90
    ph: 7
    shadowing: false
    staining: false
    temperature:
      unit: K
      value: 300
    vitrification: false
    vitrification_cryogen: None

```
## EMDataset-invalid-001
### Input
```yaml
acquisition:
  binning_camera: 2
  date_time: '2024-01-01'
  detector: Falcon 4i
  detector_mode: counting
  dose_per_movie:
    unit: "e/\u212B\xB2"
    value: 0.5
  holder: testitest
  pixel_size:
    unit: "\u212B"
    value: 1.2
authors:
- country: Switzerland
  email: john.doe@gmail.com
  first_name: John
  name: Doe
  name_org: University of Blub
  orcid: ORCID_123124151231
  type_org: Academic
  work_phone: '+4132112312'
- country: Switzerland
  email: jane.doe@gmail.com
  first_name: Jane
  name: Doe
  name_org: University of Blub
  orcid: ORCID_123124151221
  type_org: Academic
  work_phone: '+4132112312'
grants:
- funder: SNF
  project_id: SNF321
- funder: SNF
  project_id: Fundingofsomekind
instrument:
  acceleration_voltage:
    unit: kV
    value: 300
  c2_aperture:
    unit: "\xB5m"
    value: 70
  cs:
    value: 2.7
  electron_source: FEG
  illumination: FloodBeam
  imaging: Brightfield
  microscope: Titan
sample:
  grid:
    film_support: false
    manufacturer: Quantifoil
    material: Au
    mesh: 300
    pretreatment_pressure:
      unit: Pa
      value: 1.0e-06
    pretreatment_time:
      unit: s
      value: 30
    pretreatment_type: Glow discharge
  ligands:
  - present: true
    smiles: OC
  molecule:
  - expression_system: Pichia kudriavzevii
    gene_name: Rib
    molecular_class: None of these
    molecular_type: polypeptide
    name_mol: Ribosome_
    natural_source: yeast
    sequence: MMKNMMKYMMMYSYKEKSEKRRWMMKREMMKYLELLNMRMNKWVKRMMMSRKRLLSRMNRLEKKNHMNDYKLMSYNFNKNSMMMKSMLSKLMMNLLENVMNGVDLKSGKSKMSGGNMMMSKPVMKENLNTVNMLFYYFLPNNKSYKYFNRMNMYLNKHMKNYKKLVKLNKNYSKSSYLLQDKLMMSNMFNNMMFNRNNMKYMNNNVNNLMSSLNMNSNNKSLYLSLLNKTLNNNLSNLYSNNNINKSIINNTLVNMSMLNNNYNNNNTTFNINNNLFNLLNLLNNNYNNNNNYNNMMSNTNMLLNNYNNNNNNNNNNKCNMHSKMKLERKNMMLNYLLKNEMMNKNQMWMSKMENNKMNNINNNNNMLKMNKENDKTNMFGYMMSYMDMLLGNMMNKSKKSNDMKMMMSKYFGLKEVNMTGMNLKYEFNNTEMLLKLMRKGMSKRKRTLSRMFRFRLKNRMPLLNDKGMLKNKMSNNLLKNLALNNNILNVEYNIKNVLFNSINNNNINNNNNNNMYNDMKDYYNNMSLENKKDLSLNNELLYKNMVGWSLLLKGKVGARKGKNRSNRMLMTKGSFKNNNLYIYNIFDDNSNNNGYTKDRLRLNYMKNSNFISYMDKSTNNGKLGMTLKVNIL
    taxonomy_id_expression: GCA_003054445.1
    taxonomy_id_source: GCA_003054445.1
  overall_molecule:
    molecular_type: Complex
    molecular_weight:
      unit: Da
      value: 3000000
    name_sample: Ribosome
    source: yeast
  specimen:
    concentration:
      unit: M
      value: 0.3
    embedding: false
    humidity:
      unit: '%'
      value: 90
    ph: 7
    shadowing: false
    staining: false
    temperature:
      unit: K
      value: 300
    vitrification: false
    vitrification_cryogen: None

```
