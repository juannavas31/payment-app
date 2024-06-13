import { create } from "./baseService";

const http = create({});

export const createPaymentService = async (data) => {
  return await http.post('/api/payments', data);
};

export const getPaymentsService = async () => {
  return await http.get('/api/payments');
};
