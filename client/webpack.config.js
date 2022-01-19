const path = require("path");
const webpack = require("webpack");
const { merge } = require("webpack-merge");
const BundleTracker = require("webpack-bundle-tracker");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const commonConfig = require("./webpack.base.config.js");

const devConfig = {
  output: {
    path: path.resolve("./build/"),
    publicPath: "http://localhost:3000/build/", // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({ path: __dirname, filename: "./webpack-stats.json" }),
    new HtmlWebpackPlugin(),
  ],

  resolve: {
    fallback: {
      url: false,
    },
  },

  devServer: {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
      "Access-Control-Allow-Headers":
        "X-Requested-With, content-type, Authorization",
    },
    port: 3000,
    client: {
      webSocketURL: {
        port: 3000,
      },
    },
  },

  devtool: "inline-source-map",
};

module.exports = merge(commonConfig, devConfig);
