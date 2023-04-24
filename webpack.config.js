const path = require("path");
const htmlPlugin = require("html-webpack-plugin");
const css = require("mini-css-extract-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
  mode: "development",
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "build"),
    filename: "main.[contentHash].js",
  },
  plugins: [
    new CleanWebpackPlugin(),
    new htmlPlugin({ template: "src/index.html" }),
    new css({ filename: "app.css" }),
  ],
  module: {
    rules: [
      { test: /\.css$/, use: [css.loader, "css-loader"] },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [
              "@babel/preset-env",
              "@babel/preset-react",
              {
                plugins: [
                  "@babel/plugin-proposal-class-properties",
                  "@babel/plugin-transform-runtime",
                ],
              },
            ],
          },
        },
      },
      {
        test: /\.(png|jpeg|gif)$/,
        use: {
          loader: "file-loader",
          options: {
            outputPath: "images",
            name: "[name].[ext]",
          },
        },
      },
    ],
  },
  devServer: {
    devMiddleware: {
      stats: "minimal",
    }
  },
};