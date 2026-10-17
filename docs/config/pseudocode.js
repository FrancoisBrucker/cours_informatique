// Langage Prism « pseudocode » pour la coloration du pseudo-code (mots-clés en français).

const grammaire = {
  'comment': {
    pattern: /(^|[^\\])#.*/,
    lookbehind: true,
    greedy: true
  },
  'string': {
    pattern: /(?:[rub]|br|rb)?(")(?:\\.|(?!\1)[^\\\r\n])*\1/i,
    greedy: true
  },
  // définition de variables : ref a type, ref a, b, c []type
  'definition': {
    pattern: /\bref[ \t]+[\p{L}_][\p{L}\p{N}_']*(?:[ \t]*,[ \t]*[\p{L}_][\p{L}\p{N}_']*)*(?:[ \t]+(?:\[\])*[\p{L}_∅][\p{L}\p{N}_]*)?/u,
    greedy: true,
    inside: {
      'keyword': /^ref/,
      'type': {
        pattern: /([\p{L}\p{N}_'][ \t]+)(?:\[\])*(?:[\p{L}_][\p{L}\p{N}_]*|∅)$/u,
        lookbehind: true,
        alias: 'class-name'
      },
      'punctuation': /,/
    }
  },
  // boucle : pour chaque <variable> de <objet>
  'boucle': {
    pattern: /\bpour chaque[ \t]+(?:\((?:[^()\n]|\([^()\n]*\))*\)|[^():\n]+?)[ \t]+de\b/u,
    greedy: true,
    inside: {
      'mot-boucle': {
        pattern: /^pour chaque|de$/,
        alias: 'keyword'
      }
    }
  },
  // définition : algorithme nom(p1: type1, p2: []type2) → type:
  'signature': {
    pattern: /(^|\s)(?:algorithme|fonction|programme|méthode)[ \t]+[\p{L}_][\p{L}\p{N}_-]*\s*\([^()]*\)(?:\s*→\s*(?:\[\])*[\p{L}_∅][\p{L}\p{N}_]*)?/u,
    lookbehind: true,
    greedy: true,
    inside: {
      'builtin': /^(?:algorithme|fonction|programme|méthode)/,
      'function': /[\p{L}_][\p{L}\p{N}_-]*(?=\s*\()/u,
      'parameter': {
        pattern: /[\p{L}_][\p{L}\p{N}_]*(?=\s*:)/u,
        alias: 'variable'
      },
      'type': {
        pattern: /((?::|→)\s*)(?:\[\])*(?:[\p{L}_][\p{L}\p{N}_]*|∅)/u,
        lookbehind: true,
        alias: 'class-name'
      },
      'operator': /→/,
      'punctuation': /[(),:]/
    }
  },
  // type tableau hors signature : []entier, [][]booléen, []T
  'type': {
    pattern: /(?:\[\])+[\p{L}_][\p{L}\p{N}_]*/u,
    alias: 'class-name'
  },
  'class-name': {
    pattern: /(\bstructure\s+)\w+/i,
    lookbehind: true
  },
  'keyword': /\b(?:_(?=\s*:)|affiche|donne|et|ET|ou|OU|si|sinon si|sinon|répéter|pour chaque|pour|rendre|ref|tant que|self|break|continue)\b/,
  'builtin': /\b(?:Type|bool|bit|int|char|float|str|entier|chiffre|booléen|bit|réel|caractère|chaîne|algorithme|fonction|structure|attributs|méthodes)\b/,
  'boolean': /\b(?:Faux|∅|Vrai)\b/,
  'number': /\b0(?:b(?:_?[01])+|o(?:_?[0-7])+|x(?:_?[a-f0-9])+)\b|(?:\b\d+(?:_\d+)*(?:\.(?:\d+(?:_\d+)*)?)?|\B\.\d+(?:_\d+)*)(?:e[+-]?\d+(?:_\d+)*)?j?(?!\w)/i,
  'operator': /[-+%=]=?|←|→|!=|≠|≤|≥|\*\*?=?|\/\/?=?|<[<=>]?|>[=>]?|[&|^~]/,
  'punctuation': /[{}[\];(),.:]/
};
// le reste de la boucle (variable, type, …) suit la grammaire générale
grammaire.boucle.inside.rest = grammaire;

export default grammaire;

// Coloration des variables déclarées dans un bloc pseudocode :
// paramètres de la signature, `ref x type`, `x: type` en début de ligne, `pour (chaque) x de`.
const IDENT = /[\p{L}_][\p{L}\p{N}_']*/gu;
const RESERVES = new Set(["algorithme", "fonction", "programme", "méthode", "structure", "attributs", "méthodes",
  "ref", "si", "sinon", "pour", "chaque", "de", "rendre", "répéter", "tant", "que", "et", "ou", "ET", "OU", "affiche", "donne",
  "self", "break", "continue", "tout", "toute", "un", "une", "else", "Else", "Vrai", "Faux", "Type", "entier", "chiffre", "booléen", "bit", "réel", "caractère", "chaîne"]);
const BOUCLE = /\bpour[ \t]+(?:chaque|tout|toute)[ \t]+(\((?:[^()\n]|\([^()\n]*\))*\)|[^():\n]+?)[ \t]+de\b/gu;
const DEFINITION = /\bref[ \t]+([\p{L}_][\p{L}\p{N}_']*(?:[ \t]*,[ \t]*[\p{L}_][\p{L}\p{N}_']*)*)/gu;
const DECLARATIONS = [
  /(?:^|[(,])[ \t]*([\p{L}_][\p{L}\p{N}_']*)[ \t]*:(?!=)/gmu,            // paramètres, x: type
];

function variablesDéclarées(code) {
  const noms = new Set();
  for (const re of DECLARATIONS) {
    for (const m of code.matchAll(re)) {
      if (!RESERVES.has(m[1])) noms.add(m[1]);
    }
  }
  // définitions : ref a type, ref a, b, c type
  for (const m of code.matchAll(DEFINITION)) {
    for (const nom of m[1].split(",")) {
      if (!RESERVES.has(nom.trim())) noms.add(nom.trim());
    }
  }
  // variables de boucle : pour chaque x de, pour chaque x, y de, pour chaque voisin v de
  for (const m of code.matchAll(BOUCLE)) {
    for (const morceau of m[1].split(",")) {
      const mots = morceau.match(IDENT) || [];
      const nom = mots[mots.length - 1];
      if (nom && !RESERVES.has(nom)) noms.add(nom);
    }
  }
  return noms;
}

function colorier(tokens, noms, Prism) {
  for (let i = 0; i < tokens.length; i++) {
    const t = tokens[i];
    if (typeof t === "string") {
      const morceaux = [];
      let dernier = 0;
      for (const m of t.matchAll(IDENT)) {
        if (!noms.has(m[0])) continue;
        if (m.index > dernier) morceaux.push(t.slice(dernier, m.index));
        morceaux.push(new Prism.Token("variable", m[0], "parameter"));
        dernier = m.index + m[0].length;
      }
      if (morceaux.length === 0) continue;
      if (dernier < t.length) morceaux.push(t.slice(dernier));
      tokens.splice(i, 1, ...morceaux);
      i += morceaux.length - 1;
    } else if (Array.isArray(t.content) && t.type !== "comment" && t.type !== "string") {
      colorier(t.content, noms, Prism);
    }
  }
}

let hookInstallé = false;
export function installerHooks(Prism) {
  if (hookInstallé) return;
  hookInstallé = true;
  Prism.hooks.add("after-tokenize", (env) => {
    if (env.language !== "pseudocode") return;
    colorier(env.tokens, variablesDéclarées(env.code), Prism);
  });
}
