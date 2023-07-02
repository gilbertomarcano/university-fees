import React from "react";
import ReactDOM from "react-dom/client";
import { ChakraProvider } from "@chakra-ui/react";
import { RouterProvider } from "react-router";
import { createBrowserRouter } from "react-router-dom";
import Login from "./pages/Login.tsx";
import Layout from "./Layout.tsx";
import Home from "./pages/Home.tsx";
import Signup from "./pages/Signup.tsx";


const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <Login />
      },
      {
        path: '/home',
        element: <Home />
      },
      {
        path: '/signup',
        element: <Signup />
      }
    ]
  },
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <ChakraProvider>
      <RouterProvider router={router} />
    </ChakraProvider>
  </React.StrictMode>
);
