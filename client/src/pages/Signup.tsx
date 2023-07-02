import * as React from "react";
import {
  Button,
  FormControl,
  FormLabel,
  Input,
  Stack,
  VStack,
  Heading,
  useToast,
  Container,
  useColorModeValue
} from "@chakra-ui/react";
import axios from "axios";
import { useNavigate } from "react-router";

const Signup = () => {
  const toast = useToast();
  const navigate = useNavigate();

  const [state, setState] = React.useState({
    username: "",
    password: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setState({ ...state, [e.target.name]: e.target.value });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!state.username || !state.password) {
      toast({
        title: "Invalid Input",
        description: "Both username and password must be provided.",
        status: "error",
        duration: 9000,
        isClosable: true,
      });
    } else {
      try {
        const { data } = await axios.post<{ token: string }>('http://localhost:8002/users/signup', {
          username: state.username,
          password: state.password,
          email: state.email,
          first_name: state.first_name,
          last_name: state.last_name
        })
        navigate('/')
      } catch (error) {
        toast({
          title: "Sign up error",
          description: error.response.data.message,
          status: "error",
          duration: 9000,
          isClosable: true,
        });
      }
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
          Sign Up
        </Heading>

        <form onSubmit={handleSubmit}>
          <Stack spacing="6">
            <FormControl id="username">
                <FormLabel>Username</FormLabel>
                <Input
                name="username"
                type="username"
                autoComplete="username"
                required
                value={state.username}
                onChange={handleChange}
                />
            </FormControl>
            <FormControl id="password">
                <FormLabel>Password</FormLabel>
                <Input
                name="password"
                type="password"
                required
                value={state.password}
                onChange={handleChange}
                />
            </FormControl>
            <FormControl id="email">
                <FormLabel>Email</FormLabel>
                <Input
                name="email"
                type="email"
                required
                value={state.email}
                onChange={handleChange}
                />
            </FormControl>
            <FormControl id="first_name">
                <FormLabel>First Name</FormLabel>
                <Input
                name="first_name"
                type="first_name"
                required
                value={state.first_name}
                onChange={handleChange}
                />
            </FormControl>
            <FormControl id="last_name">
                <FormLabel>Last Name</FormLabel>
                <Input
                name="last_name"
                type="last_name"
                required
                value={state.last_nmame}
                onChange={handleChange}
                />
            </FormControl>
            <Button type="submit" colorScheme="teal" size="lg" fontSize="md">
                Sign Up
            </Button>
            <Button colorScheme="teal" size="lg" fontSize="md" variant="outline" onClick={() => navigate('/')}>
                Login
            </Button>
          </Stack>
        </form>
      </VStack>
    </Container>
  );
};

export default Signup;