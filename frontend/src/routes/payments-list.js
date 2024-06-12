import { Link } from "react-router-dom";
import { useState } from "react";
import { listData } from "../services/ListService";

function PaymentsList() {

  const [payments, setPayments] = useState([]);
  listData().then((list) =>
    setPayments(list)
);
  return (
    <>
      <div>
        <Link to="/create">New Payment</Link>
      </div>
      <div>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Card Number</th>
              <th>Currency</th>
              <th>Amount</th>
            </tr>
          </thead>
          <tbody>
            {payments.map((payment) => (
              <tr key={payment.id}>
                <td>{payment.id}</td>
                <td>{payment.name}</td>
                <td>{payment.cardNumber}</td>
                <td>{payment.currency}</td>
                <td>{payment.amount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default PaymentsList;
