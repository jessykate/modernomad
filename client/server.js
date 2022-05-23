var webpack = require("webpack");
var WebpackDevServer = require("webpack-dev-server");
const { merge } = require("webpack-merge");

var config = require("./webpack.config");

new WebpackDevServer(webpack(merge(config, { mode: "development" })), {
  hot: true,
  historyApiFallback: true,
}).listen(3000, "0.0.0.0", function (err, result) {
  if (err) {
    console.log(err);
  }

  console.log("Listening at 0.0.0.0:3000");
});
