module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
    ? '/revue/'
    : '/',
    outputDir: "../docs"
}