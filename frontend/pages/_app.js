import App from 'next/app'
import React from 'react'
import { ApolloProvider } from '@apollo/react-hooks'
import withApolloClient from '../lib/with-apollo-client'
import {AppContext} from "../AppContext";
import cookie from "js-cookie";
import i18next from "i18next";
import Layout from "../components/Layout";
import '../assets/fonts/fonts.sass'
import '../assets/helpers.sass'
import 'semantic-ui-css/semantic.min.css'


class MyApp extends App {

  render () {
    const { Component, pageProps, apolloClient } = this.props;

    let language = pageProps.cookies.language;
    if (!language){
        cookie.set('language','ru');
        language = 'ru';
    }

    i18next.init({
        lng: language,
        resources: require(`../languages/${language}.json`)
    });

    return (
      <ApolloProvider client={apolloClient}>
        <AppContext.Provider value={pageProps.cookies}>
            <Layout>
                <Component {...pageProps} />
            </Layout>
        </AppContext.Provider>
      </ApolloProvider>
    )
  }
}

export default withApolloClient(MyApp)
