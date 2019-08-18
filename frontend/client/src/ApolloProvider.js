import React from 'react'
import App from './App'
import ApolloClient from "apollo-client"
import {InMemoryCache} from "apollo-cache-inmemory"
import {createHttpLink} from "apollo-link-http"
import { ApolloProvider } from '@apollo/react-hooks'

const httpLink = createHttpLink({
    uri: "http://192.168.0.95:8000/graphql"
});

const client = new ApolloClient({
    link: httpLink,
    cache: new InMemoryCache()
});

export default (
    <ApolloProvider client={client}>
        <App/>
    </ApolloProvider>
)