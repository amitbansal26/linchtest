console.log("This is a test node script from the node hook")
process.argv.forEach(function (val, index, array) {
  console.log(index + ': ' + val);
});
