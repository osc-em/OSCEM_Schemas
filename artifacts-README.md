# OSC-EM Schema Artifacts

This directory contains the generated schema artifacts in various formats.

## Structure

```
artifacts/
├── latest/              # Always points to the most recent release
│   ├── spa/
│   ├── cellular_tomo/
│   ├── env_tomo/
│   ├── general/
│   └── subtomo/
└── v1.0.0/             # Specific version
    ├── spa/
    ├── cellular_tomo/
    ├── env_tomo/
    ├── general/
    └── subtomo/
```

Each schema directory contains:
- `jsonschema/` - JSON Schema for validation
- `jsonld/` - JSON-LD context and schema
- `owl/` - OWL ontology
- `graphql/` - GraphQL schema
- `shex/` - ShEx schema
- `shacl/` - SHACL constraints
- `protobuf/` - Protocol Buffers definition
- `sqlschema/` - SQL schema
- `excel/` - Excel representation

## Permanent URLs via w3id

These artifacts are accessible via permanent w3id URLs:

- Latest: `https://w3id.org/osc-em/oscem-schemas/spa/jsonschema`
- Versioned: `https://w3id.org/osc-em/oscem-schemas/v1.0.0/spa/jsonschema`

## Direct GitHub Pages URLs

Alternatively, you can access them directly:

- Latest: `https://osc-em.github.io/oscem-schemas/artifacts/latest/spa/jsonschema/oscem_schemas_spa.schema.json`
- Versioned: `https://osc-em.github.io/oscem-schemas/artifacts/v1.0.0/spa/jsonschema/oscem_schemas_spa.schema.json`
