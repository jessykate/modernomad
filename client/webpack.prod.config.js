const path = require("path");

const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const { merge } = require("webpack-merge");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");

const commonConfig = require("./webpack.base.config.js");

const prodConfig = {
  output: {
    path: path.resolve("./dist"),
  },

  plugins: [
    new BundleTracker({ filename: "./webpack-stats-prod.json" }),
    // removes a lot of debugging code in React
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],

  // minifies your code
  optimization: {
    minimizer: [new UglifyJsPlugin()],
  },
};

module.exports = merge(commonConfig, prodConfig);
