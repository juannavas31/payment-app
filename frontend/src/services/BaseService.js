import axios from "axios";

export const create = (opts) => {
  const http = axios.create({
    // baseURL: process.env.urlAPI || "http://141.95.108.196:3000",
    ...opts,
  });

  http.interceptors.response.use(
    (response) => response.data,
    (error) => {
      if (
        error.response &&
        [500].includes(error.response.data.status)
      ) {
        console.log("Error 500")
      }
      return Promise.reject(error?.response);
    }
  );

  return http;
};
