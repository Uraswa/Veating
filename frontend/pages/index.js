import React,{useContext} from 'react'
import { Button } from 'semantic-ui-react'
import i18next from "i18next";
import PageInit from '../pageInit';


const IndexPage = () => {

   return (
        <div className="container" >
           <Button >{i18next.t('test_message')}</Button>
        </div>
    );
};

IndexPage.getInitialProps = PageInit;

export default IndexPage