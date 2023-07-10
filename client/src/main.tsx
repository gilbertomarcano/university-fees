import React from "react";
import ReactDOM from "react-dom/client";
import { ChakraProvider } from "@chakra-ui/react";
import { RouterProvider } from "react-router";
import { createBrowserRouter } from "react-router-dom";
import Login from "./pages/Login.tsx";
import Layout from "./Layout.tsx";
import Home from "./pages/Home.tsx";
import Signup from "./pages/Signup.tsx";
import CompleteSignup from "./pages/CompleteSignup.tsx";
import Admin from "./pages/Admin.tsx";
import UserList from "./pages/ListUsers.tsx";


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
        path: '/admin',
        element: <Admin />
      },
      {
        path: '/users',
        element: <UserList />
      },
      {
        path: '/signup',
        element: <Signup />
      },
      {
        path: '/signup/:id/complete',
        element: <CompleteSignup />
      }
    ]
  },
  // {
  //   path: "/",
  //   children: [
  //     {
  //       path: '/users',
  //       element: <UserList />
  //     },
  //   ]
  // },
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <ChakraProvider>
      <RouterProvider router={router} />
    </ChakraProvider>
  </React.StrictMode>
);
