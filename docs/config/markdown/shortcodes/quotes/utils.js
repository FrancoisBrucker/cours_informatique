export function escapeHtml(code) {
    return "\n\n" + code + "\n\n";
}

export function template(content, arg) {
    let component = "";
    if (arg) {
        component += `<div class="pl-8 mb-2 mr-8">${escapeHtml(arg)}</div>`;
    }
    component += `<div class="pl-8 mr-8">${escapeHtml(content)}</div></div>`;

    return component;
}