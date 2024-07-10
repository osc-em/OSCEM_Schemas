const Ajv = require('ajv/dist/2019');
const fs = require('fs');


const data = JSON.parse(fs.readFileSync('data_valid_sample.json', 'utf8'))
//console.log(data);
const mySchema = JSON.parse(fs.readFileSync('schema_sample_forajv.json', 'utf8'))
//console.log(mySchema);
const ajv = new Ajv()

const validate = ajv.compile(mySchema);
const valid = validate(data);

if (valid) {
  console.log('Data is valid!');
} else {
  console.error('Data is invalid:', validate.errors);
}
