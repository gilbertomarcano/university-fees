import { Container } from "@chakra-ui/react"
import { Outlet } from "react-router"

const Layout = () => {
    return (
        <Container py={6}>
            <Outlet />
        </Container>
    )
}

export default Layout