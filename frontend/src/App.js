import { createBrowserRouter, RouterProvider } from "react-router-dom";
import PaymentCreate from "./routes/payment-create.js";
import PaymentsList from "./routes/payments-list.js";

const routes = [
  {
    path: "/",
    element: <PaymentsList />,
  },
  {
    path: "/create",
    element: <PaymentCreate />,
  },
];

function App() {
  const router = createBrowserRouter(routes);
  return <RouterProvider router={router} />;
}

export default App;
