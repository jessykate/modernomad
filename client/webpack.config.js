var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  context: __dirname,
  entry: [
    "webpack-dev-server/client?http://localhost:3000",
    "webpack/hot/only-dev-server",
    "./js/index",
  ],

  output: {
    path: path.resolve("./build/"),
    filename: "[name]-[hash].js",
    publicPath: "http://localhost:3000/build/", // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({ path: __dirname, filename: "./webpack-stats.json" }),
  ],

  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env", "@babel/preset-react"],
          },
        },
      }, // to transform JSX into JS
    ],
  },

  resolve: {
    extensions: ["", ".js", ".jsx"],
    fallback: {
      url: false,
    },
  },
};
