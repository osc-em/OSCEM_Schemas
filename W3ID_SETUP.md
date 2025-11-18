# w3id Configuration for OSC-EM Schemas

This file shows the configuration needed for your w3id namespace.
You'll need to submit a PR to: https://github.com/perma-id/w3id.org

## File: `oscem-schemas/.htaccess`

Place this in the w3id.org repository at: `oscem-schemas/.htaccess`

```apache
# OSC-EM Schemas w3id Configuration
# Redirect to GitHub Pages artifacts

Options +FollowSymLinks
RewriteEngine on

# Redirect latest version
RewriteRule ^latest/(.+)$ https://osc-em.github.io/oscem-schemas/artifacts/latest/$1 [R=302,L]

# Redirect specific versions (e.g., v1.0.0, v1.2.3)
RewriteRule ^(v[0-9]+\.[0-9]+\.[0-9]+)/(.+)$ https://osc-em.github.io/oscem-schemas/artifacts/$1/$2 [R=302,L]

# Default: redirect to documentation
RewriteRule ^$ https://osc-em.github.io/oscem-schemas/ [R=302,L]
```

## Example URLs

After configuration, these permanent URLs will work:

### Latest version (302 redirect - changes with releases)
- `https://w3id.org/osc-em/oscem-schemas/latest/spa/jsonschema/oscem_schemas_spa.schema.json`
- `https://w3id.org/osc-em/oscem-schemas/latest/cellular_tomo/owl/oscem_schemas_cellular_tomo.owl.ttl`

### Specific version (302 redirect - permanent)
- `https://w3id.org/osc-em/oscem-schemas/v1.0.0/spa/jsonschema/oscem_schemas_spa.schema.json`
- `https://w3id.org/osc-em/oscem-schemas/v1.2.3/env_tomo/jsonld/oscem_schemas_env_tomo.jsonld`

### Root (redirects to docs)
- `https://w3id.org/osc-em/oscem-schemas/`

## Setup Instructions

1. Fork https://github.com/perma-id/w3id.org
2. Create directory: `oscem-schemas/`
3. Add the `.htaccess` file above
4. Create a `README.md` explaining your namespace
5. Submit a Pull Request
6. Once merged, your permanent URLs are live!

## Testing Before Submission

You can test the redirects locally or use GitHub Pages directly until w3id is set up:
- Direct: `https://osc-em.github.io/oscem-schemas/artifacts/latest/spa/jsonschema/...`
