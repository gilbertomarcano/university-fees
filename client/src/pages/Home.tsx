import * as React from 'react';
import {
  Box,
  Heading,
  Text,
  Avatar,
  Flex,
  Stack,
  Spinner,
  Button,
  useColorModeValue,
  VStack,
  Container,
} from '@chakra-ui/react';
import axios from 'axios';
import { useNavigate } from 'react-router';

const Home = () => {
  const [user, setUser] = React.useState(null);
  const fetchUserBg = useColorModeValue('gray.200', 'gray.600');
  const navigate = useNavigate();

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem('token');
        const { data } = await axios.get(`${import.meta.env.VITE_BACKEND_URL}/users/me`, {
          headers: { Authorization: `Token ${token}` },
        });
        setUser(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchData();
  }, []);

  const handleLogout = async () => {
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

  if (!user) {
    return <Spinner />;
  }

  return (
    <Container height="100vh" display="flex" flexDirection="column" justifyContent="center">
      <Flex justify="center" mt={12}>
        <VStack
          flexGrow={0}
          boxShadow={'2xl'}
          p={8}
          mr={6}
          rounded={'xl'}
          bg={useColorModeValue('white', 'gray.800')}
          spacing={6}
          width="100%"
          maxWidth={{ base: '90%', md: '80%', lg: '60%' }}
        >
          <Box textAlign="center">
            <Avatar size="2xl" name={user.name} />
            <Heading fontSize="2xl">Welcome, {user.first_name} {user.last_name}</Heading>
          </Box>
          <Box textAlign="center">
            <Text fontWeight="bold">Username:</Text>
            <Text>{user.username}</Text>
          </Box>
          <Box textAlign="center">
            <Text fontWeight="bold">Email:</Text>
            <Text>{user.email}</Text>
          </Box>
          {/* Add other user fields as required */}
          <Button onClick={handleLogout} type="submit" colorScheme="red" size="lg" fontSize="md">
            Log Out
          </Button>
        </VStack>
      </Flex>
    </Container>
  );
};

export default Home;