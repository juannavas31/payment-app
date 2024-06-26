import { useNavigate } from "react-router";
import { createPaymentService } from "../services/paymentService";

function PaymentCreate() {
  const navigate = useNavigate();

  // The payment can be created with `POST /api/payments`
  const submit = (ev) => {
    ev.preventDefault();

    // Create object with new payment details from the submitted form.
    const payment = Object.fromEntries(new FormData(ev.target));
    console.log(payment);

    // Call the `createPaymentService` function from the `createPaymentService` and pass the payment
    createPaymentService(payment)
      .then(() => {
        navigate("/");
      })
      .catch((error) => {
        console.log("Error :", error);
      });
  }

  return (
    <form onSubmit={submit}>
      <div>
        <label>Name</label>
        <input type="text" name="name" required/>
      </div>
      <div>
        <label>Card Number</label>
        <input type="text" name="cardNumber" required/>
      </div>
      <div>
        <label>Currency</label>
        <select name="currency" required>
          <option value=""></option>
          <option value="EUR">EUR</option>
          <option value="GBP">GBP</option>
          <option value="USD">USD</option>
        </select>
      </div>
      <div>
        <label>Amount</label>
        <input type="text" name="amount" required/>
      </div>
      <div>
        <button type="submit">Create</button>
      </div>
    </form>
  );
}

export default PaymentCreate;
