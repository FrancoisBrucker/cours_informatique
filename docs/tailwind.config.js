module.exports = {
    content: ["./src/**/!(node_modules)/**/*.{html,js,njk}",
              "./config/markdown/shortcodes/quotes/!(index).js"],
    theme: {
      extend: {},
    },
    plugins: [
      require('@tailwindcss/typography'),
    ],
    
  }