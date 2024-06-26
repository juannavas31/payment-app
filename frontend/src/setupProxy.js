const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/api",
    createProxyMiddleware({
      target: `http://localhost:3001`,
      // target: `http://localhost:${process.env.BACKEND_PORT}`,
      changeOrigin: true,
    })
  );
};
