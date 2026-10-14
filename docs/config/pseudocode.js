// Langage Prism « pseudocode » pour la coloration du pseudo-code (mots-clés en français).

export default {
  'comment': {
    pattern: /(^|[^\\])#.*/,
    lookbehind: true,
    greedy: true
  },
  'string': {
    pattern: /(?:[rub]|br|rb)?(")(?:\\.|(?!\1)[^\\\r\n])*\1/i,
    greedy: true
  },
  'function': {
    pattern: /((?:^|\s)(algorithme|fonction|programme|méthode)[ \t]+)[a-zA-Z_]\w*(?=\s*\()/g,
    lookbehind: true
  },
  'class-name': {
    pattern: /(\bstructure\s+)\w+/i,
    lookbehind: true
  },
  'keyword': /\b(?:_(?=\s*:)|affiche|donne|et|ET|ou|OU|si|sinon si|sinon|répéter|pour chaque|pour|rendre|tant que|self|break|continue)\b/,
  'builtin': /\b(?:Type|entier|chiffre|booléen|bit|réel|caractère|chaîne|algorithme|fonction|structure|attributs|méthodes)\b/,
  'boolean': /\b(?:Faux|∅|Vrai)\b/,
  'number': / [ijn]([0-9])*(')*[\n ]|\b0(?:b(?:_?[01])+|o(?:_?[0-7])+|x(?:_?[a-f0-9])+)\b|(?:\b\d+(?:_\d+)*(?:\.(?:\d+(?:_\d+)*)?)?|\B\.\d+(?:_\d+)*)(?:e[+-]?\d+(?:_\d+)*)?j?(?!\w)/i,
  'operator': /[-+%=]=?|←|→|!=|≠|≤|≥|:=|\*\*?=?|\/\/?=?|<[<=>]?|>[=>]?|[&|^~]/,
  'punctuation': /[{}[\];(),.:]/
};
