import React,{useContext} from 'react'
import 'semantic-ui-css/semantic.min.css'
import { Button } from 'semantic-ui-react'
import i18next from "i18next";
import Layout from "../components/Layout";
import {AppContext} from '../AppContext'
import PageInit from '../pageInit';


const IndexPage = () => {

    const context = useContext(AppContext);
    console.log(context);

    return (
        <Layout>
            <div className="container">
                <Button>{i18next.t('test_message')}</Button>
            </div>
        </Layout>

    );
};

IndexPage.getInitialProps = PageInit;

export default IndexPage