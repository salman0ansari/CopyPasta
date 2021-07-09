const axios = require('axios');

const getCP = async (lang) => {
    try {
        req = await axios.get(`https://copy-pasta-pi.vercel.app/${lang}/1`);
        const {title,text} = req.data[0];
        return {title,text}
    } catch (e) {
        console.log(e);
    }
};

module.exports = getCP;