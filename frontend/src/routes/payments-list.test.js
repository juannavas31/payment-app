import React from 'react';
import ReactDOM from 'react-dom/client';
import { act } from 'react-dom/test-utils';
import { findByText, render, screen, waitFor } from "@testing-library/react";
import { MemoryRouter as Router } from 'react-router-dom';
import PaymentsList from "./payments-list";
import * as paymentService from "../services/paymentService";

const mockPayments = [
    {
        id: "1234567",
        name: "John Doe",
        cardNumber: "1234-5678-9012-4444",
        currency: "USD",
        amount: "100"
    }
];

let container;

beforeEach(() => {
    container = document.createElement('div');
    document.body.appendChild(container);
  });
  
  afterEach(() => {
    document.body.removeChild(container);
    container = null;
  });  

test("renders PaymentsList component", async () => {
    // arrange
    jest.spyOn(paymentService, "getPaymentsService").mockResolvedValue(mockPayments);

    //act
    act(() => {
        ReactDOM.createRoot(container).render(
            <Router>
                <PaymentsList />    
            </Router>);
    });
    
    //assert
    const linkElement = screen.getByText(/New Payment/i);
    expect(linkElement).toBeInTheDocument();
    const idHeader = screen.getByText(/ID/i);
    expect(idHeader).toBeInTheDocument();

    expect(await findByText(container, mockPayments[0].id)).toBeInTheDocument();
    expect(await findByText(container, mockPayments[0].name)).toBeInTheDocument();
    expect(await findByText(container, mockPayments[0].cardNumber)).toBeInTheDocument();
    expect(await findByText(container, mockPayments[0].currency)).toBeInTheDocument();
    expect(await findByText(container, mockPayments[0].amount)).toBeInTheDocument();
});