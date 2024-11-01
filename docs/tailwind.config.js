import typography from '@tailwindcss/typography';

export default {
    mode: 'jit',
    content: [
        "./src/assets/stylesheets/*.{html,js,njk}",
        "./src/*.{html,js,njk}",
        "./src/_includes/**/*.{html,js,njk}",
        "./src/cs/**/*.{html,js,njk}",
        "./src/mon/**/*.{html,js,njk}",
        "./src/pok/**/*.{html,js,njk}",
        "./src/projets/**/*.{html,js,njk}",
        "./config/markdown/shortcodes/quotes/!(index).js"
    ],
    theme: {
    extend: {},
    },
    plugins: [
        typography,
    ],
}