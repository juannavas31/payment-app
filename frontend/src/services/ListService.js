import { create } from "./BaseService";

const http = create({});

export const listData = async () => {
  return await http.get('/api/payments');
};
