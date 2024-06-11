# Ebury Full Stack JavaScript & Python Test

## About the project

The project is a fairly typical but simplified example of a payment application.

The application displays existing payments and allows the user to create new payments by completing a form.

However, a number of tasks have been left for you, the developer, to complete.

To get started:

- Install dependencies in each of the following directories: `./`, `./frontend` using `npm install`.
- Run `npm start` in the project's root directory to start the frontend.

If there are any errors you may need to change `./.env` to pick unused ports.

## Project Structure

The root directory is only a container for the components of the example application - frontend, backend, and payment API.

The `./.env` (dotenv) file controls the port each component runs on. You may need to change this if the ports are already in use on your computer.

Running `npm start` in the root directory will start all components of the application and should be sufficient for the purpose of this test. Pressing Ctrl-C will stop everything.

### frontend

`./frontend` contains a React application. It will auto-reload and update the browser when files change.

The frontend consists of two pages:

- The main page displays a simple, tabular view of current payments.
- A form page creates a new payment.

### backend

`./backend` contains a FastAPI server to act as a backend for the frontend. It will auto-reload when files change.

The `frontend` proxies requests for `/api/*` to the `backend` (see ./frontend/src/setupProxy.js) so the `backend` is available on the same URL.

The `backend`'s `/api/*` is responsible for making the `payment-api` available from the `frontend`.

### payment-api

`./payment-api` contains a FastAPI server to simulate an internal API. It will auto-reload when files change.

The payment API consists of two endpoints:

- GET /api/payments - returns a list of existing payments
- POST /api/payments - creates a new payment

For the purpose of the test, payment data can be stored in memory.

## Tasks to Complete

There are many improvements that _could_ be made but as a guideline: please focus on the tasks below, don't worry too much about the user interface, do focus on production quality services.

Feel free to express your preferences, opinions, and strengths where appropriate.

Please avoid moving files and code unnecessarily to allow reviewers to easily see what was changed.

Tasks:

1. Fetch and display the list of existing payments

   Update the `PaymentsList` page to display the current list of payments from the `payment-api`.

   The `payment-api` returns some example payments by default.

2. Handle the form submit to create new payments

   Implement the form on the `PaymentCreate` page to collect data and create a new payment from that data.

   All payment details entered by the user are required.

   The browser should redirect to the list page where the new, valid payment will be visible.

3. Protect the `payment-api` with an API key

   No-one should have access to an internal service unless authorized. Ensure all requests to the `payment-api` include a valid API key.

   The API key should be a static or hard-coded value. An environment variable would be a good place to configure the key.

4. Assign each new payment a unique `id`

   Generate an ID for each new payment's `id` when created.

   The ID must be:

   - Unique, for all payments
   - 7 characters long
   - Made up of the characters "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ".

   Examples of valid IDs are "78GBM5F", "BH6G89N", etc.

   Note: example payments deliberately include a "~" so they will not clash.
