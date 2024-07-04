const path = require("path");
const webpack = require("webpack");
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: "./src/index.jsx",  // Changed to .jsx if your entry file is JSX
  mode: process.env.NODE_ENV || 'development',
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js",
    publicPath: '/static/frontend/',  // Add this line
  },
  devtool: 'source-map',
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,  // Changed to support both .js and .jsx
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        },
      },
      {
        test: /\.module\.css$/,  // Use .module.css for CSS modules
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              modules: true,
              importLoaders: 1,
            }
          }
        ],
      },
      {
        test: /\.css$/,  // Regular CSS files
        exclude: /\.module\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'development'),
    }),
    new CopyPlugin({
      patterns: [
        { from: 'public', to: 'public' }
      ],
    }),
  ],
  devServer: {
    historyApiFallback: true,
    contentBase: './dist',
  },
  stats: {
    errorDetails: true,
  },
};