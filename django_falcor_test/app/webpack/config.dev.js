const webpack = require('webpack');

const makeConfig = require('./config.base');


const filenameTemplate = '[name]';

const config = makeConfig({
    filenameTemplate: filenameTemplate,

    devtool: 'cheap-module-eval-source-map',
    
    extractCss: false,

    // This must be same as Django's STATIC_URL setting
    publicPath: '/static/',

    plugins: [
    ],
});
console.log("Using DEV config");


module.exports = config;
