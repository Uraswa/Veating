import React from 'react'
import './style.sass'
import i18next from "i18next";
import { Dropdown,Button,Icon } from 'semantic-ui-react'
import {categories} from "../../../constants";
import Link from 'next/link'
import { useRouter } from 'next/router'


export default (props) => {
    const router = useRouter();
    console.log(router);
    return (
        <nav id="siteNav" className="d-flex">
            <div className="ui container siteNav__body">
                <div className="search d-flex align-center">
                    <form action="" className="d-flex ">
                        <div className="d-flex align-center">
                            <Dropdown
                                placeholder={i18next.t('select_category')}
                                id="category-select"
                                clearable
                                options={categories.map((v,i) => {
                                return {...v,text:i18next.t(v.text)}
                            })} selection />
                        </div>
                        <div className="form-second-block d-flex">
                            <input type="text" placeholder={i18next.t('search_producs')}/>
                            <Button icon>
                                <Icon name='search' />
                            </Button>
                        </div>
                    </form>
                 </div>
                <ul>
                    {[{text:'home',value:-2,'route':'/'},...categories, {text:'blog',value:-1}].map((v,i) => {
                        return (
                            <Link href='/' key={v.value}>

                                <li className={ router.route == v.route ? 'active' : '' } >
                                    {i18next.t(v.text)}
                                </li>

                            </Link>
                        )
                    })}
                </ul>
            </div>
        </nav>

    )
}