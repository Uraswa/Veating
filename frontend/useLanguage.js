import cookie from "js-cookie";
import i18next from "i18next";


export default ({language}) => {

    if (!language){
        cookie.set('language','ru');
        language = 'ru';
    }

    i18next.init({
        lng: language,
        resources: require(`./languages/${language}.json`)
    });
}