import React from 'react'
import './style.sass'
import i18next from "i18next";


export default (props) => {
    return (
        <section id="topHeader">
            <div className="ui container">
                USD
                English
                {i18next.t('login')}
                {i18next.t('register')}
            </div>
        </section>
    )
}