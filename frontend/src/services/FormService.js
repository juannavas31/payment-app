import { create } from "./BaseService";

const http = create({});

export const paymentData = async (data) => {
  return await http.post('/api/payments', data);
};
