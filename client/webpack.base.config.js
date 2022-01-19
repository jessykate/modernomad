var path = require("path");

module.exports = {
  context: __dirname,
  entry: "./js/index",

  output: {
    path: path.resolve("./build/"),
    filename: "[name]-[hash].js",
  },

  plugins: [],

  resolve: {
    extensions: ["", ".js", ".jsx"],
  },
};
