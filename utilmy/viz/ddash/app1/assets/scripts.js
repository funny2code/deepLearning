const PATH = {
    'links':'about:blank',
    'html':'assets/html/',
    'dash':'pages/'
}

const NUMERIC = new RegExp(/^[0-9]*$/)
const VALID_LINKS = new RegExp('^(http[s]?:\\/\\/(www\\.)?|www\\.){1}([0-9A-Za-z-\\.@:%_\+~#=]+)+((\\.[a-zA-Z]{2,3})+)(/(.)*)?(\\?(.)*)?')

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        render: function(contentType, targetRender, homePage) {
            if (targetRender.length == 0){
                if (contentType == 'links'){
                    homePage = VALID_LINKS.test(homePage) ? homePage : PATH[contentType]
                    return homePage
                }
                return `${PATH[contentType]}${homePage}`
            }

            let target = targetRender[0]
            if (!NUMERIC.test(target)){
               
                if (contentType == 'links'){
                    if (VALID_LINKS.test(target)){
                        return target
                    } 
                } else if ((contentType == 'html')){
                    if (target.endsWith('.html')) {
                        return `${PATH[contentType]}${target}`
                    } 
                    
                } else if (contentType == 'dash') {
                        return `${PATH[contentType]}${target}`
                }
            }
            
            return dash_clientside.no_update 
            
        }
    }
});