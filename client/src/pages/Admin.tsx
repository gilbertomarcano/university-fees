import * as React from 'react';
import {
  Box,
  Heading,
  Button,
  useColorModeValue,
  VStack,
  Container,
} from '@chakra-ui/react';
import axios from "axios";
import { useNavigate } from 'react-router';

const Admin = () => {
  const navigate = useNavigate();
  const adminBg = useColorModeValue('gray.200', 'gray.600');

  const handleNewUser = () => {
    navigate('/signup');
  }

  const handleListUsers = () => {
    navigate('/users');
  }

  const handleLogout = async () => {
    console.log("XD")
    try {
      const token = localStorage.getItem('token');
      await axios.post(`${import.meta.env.VITE_BACKEND_URL}/users/logout`, {}, {
        headers: { Authorization: `Token ${token}` },
      });
      localStorage.removeItem('token');
      navigate('/');
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <Container
      height="100vh"
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
    >
      <VStack
        boxShadow={'2xl'}
        p={8}
        rounded={'xl'}
        bg={useColorModeValue('white', 'gray.800')}
        spacing={6}
        width="100%"
        maxWidth={{ base: '90%', md: '80%', lg: '60%' }}
      >
        <Heading textAlign="center" size="xl" fontWeight="extrabold">
          Admin Dashboard
        </Heading>
        <Button onClick={handleNewUser} type="button" width="80%" colorScheme="blue" size="lg" fontSize="md">
          Sign Up New User
        </Button>
        <Button onClick={handleListUsers} type="button" width="80%" colorScheme="teal" size="lg" fontSize="md">
          List Users
        </Button>
        <Button onClick={handleLogout} colorScheme="teal" size="lg" width="80%" fontSize="md" variant="outline">
          Logout
        </Button>
      </VStack>
    </Container>
  );
};

export default Admin;
