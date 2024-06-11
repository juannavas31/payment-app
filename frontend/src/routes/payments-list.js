import { Link } from "react-router-dom";

function PaymentsList() {
  // The list of payments is available from `GET /api/payments`
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
            <tr>
              <td>...</td>
              <td>...</td>
              <td>...</td>
              <td>...</td>
              <td>...</td>
            </tr>
          </tbody>
        </table>
      </div>
    </>
  );
}

export default PaymentsList;
