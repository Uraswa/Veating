import Wrapper from '../AppContext'
import React from 'react'
import pageInit from "../pageInit";
import { Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'


const IndexPage = ({cookies}) => {

    return (
        <Wrapper cookies={cookies}>
            <div class="container">
            <Button variant="warning">P</Button>
            </div>
        </Wrapper>
    );
};

IndexPage.getInitialProps = pageInit;

export default IndexPage