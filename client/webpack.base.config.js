module.exports = {
  context: __dirname,
  entry: ["./js/index"],

  output: {
    filename: "[name]-[hash].js",
  },

  resolve: {
    extensions: ["", ".js", ".jsx"],
  },

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
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
};
