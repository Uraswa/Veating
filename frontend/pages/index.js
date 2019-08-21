import Wrapper from '../AppContext'
import React from 'react'
import pageInit from "../pageInit";
import 'semantic-ui-css/semantic.min.css'
import { Button } from 'semantic-ui-react'


const IndexPage = ({cookies}) => {

    return (
        <Wrapper cookies={cookies}>
            <div class="container">
                <Button>Click Here</Button>
            </div>
        </Wrapper>
    );
};

IndexPage.getInitialProps = pageInit;

export default IndexPage