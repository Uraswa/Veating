import Wrapper from '../AppContext'
import React from 'react'
import pageInit from "../pageInit";
import 'semantic-ui-css/semantic.min.css'
import { Button } from 'semantic-ui-react'
import i18next from "i18next";
import useLanguage from "../useLanguage";


const IndexPage = ({cookies}) => {
    useLanguage(cookies);

    return (
        <Wrapper cookies={cookies}>
            <div className="container">
                <Button>{i18next.t('test_message')}</Button>
            </div>
        </Wrapper>
    );
};

IndexPage.getInitialProps = pageInit;

export default IndexPage