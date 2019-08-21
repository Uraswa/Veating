import React,{ useContext,useEffect } from 'react'
import Link from 'next/link'
import { withRouter } from 'next/router'
import TopHeader from "./TopHeader/topHeader"
import MiddleHeader from './MiddleHeader/MiddleHeader'
import SiteNavigation from "./SiteNavigation/SiteNavigation";


const Header = ({ router: { pathname } }) => {
  return (
  <header>
    <TopHeader/>
    <MiddleHeader/>
    <SiteNavigation/>
  </header>
)};

export default withRouter(Header)
