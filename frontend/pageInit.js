import cookie from "cookie";


export default ({req}) => {
    const cookies = cookie.parse(req ? req.headers.cookie || "" : document.cookie);
    return {cookies}
}