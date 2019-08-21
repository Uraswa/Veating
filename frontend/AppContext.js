import React, {createContext} from 'react'
import Layout from "./components/Layout";

export const AppContext = createContext({});

export default ({ children,cookies }) => {
    return  (
        <AppContext.Provider value={cookies}>
            <Layout>{children}</Layout>
        </AppContext.Provider>
    )
}