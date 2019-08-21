import React,{Fragment} from 'react'
import Header from "./Header";
import Footer from "./Footer";

export default ({ children }) => (
  <Fragment>
    <Header/>
    <main>
        {children}
    </main>
    <Footer/>
  </Fragment>
)
