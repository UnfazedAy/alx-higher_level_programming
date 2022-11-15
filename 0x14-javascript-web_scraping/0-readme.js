const fs = require('fs');
const { argv } = require('process');
let filePath = argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err.message);
  } else {
    console.log(data.toString());
  }
});
