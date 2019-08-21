import React,{Fragment} from 'react'
import Header from "./Header/Header";
import Footer from "./Footer";



export default ({ children }) => {

  return (
   <Fragment>
    <Header/>
    <main>
        {children}
    </main>
    <Footer/>
  </Fragment>
)}
