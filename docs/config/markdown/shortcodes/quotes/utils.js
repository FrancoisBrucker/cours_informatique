module.exports = {
    escapeHtml: (code) => {
        return "\n\n" + code + "\n\n"
    },
    template: (content, arg) => {
        var component = "";
        if (arg) {
            component += `<div class="pl-8  mb-2 mr-2">${escapeHtml(arg)}</div>`
        }
        component += `<div class="pl-8 mr-2">${escapeHtml(content)}</div></div>`

        return component;

    }
};


function escapeHtml(code) {
    return "\n\n" + code + "\n\n"
}
