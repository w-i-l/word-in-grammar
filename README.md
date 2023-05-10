<h1>Grammar word checking</h1>
<h2>Check if a given word is in a grammar</h2>
<img src='https://github.com/w-i-l/word-in-grammar/assets/65015373/bcdeede3-0810-4623-9d4c-faf222b9ccba'>



<br>
<hr>
<h2>How to use it</h2>

<h3>File format</h3>

<p>The grammar should be in a <code>.txt</code> file, following these rules:<p>

<ul>
    <li>the first line is the start point for the grammar</li>
    <li>the nonterminating symbols should be in <code>Capitalized</code> case.</li>
    <li>the products for a single nonterminating symbol can be written on many lines</li>
    <li>the structure for a line is the following:</li>
    <code><b>Nonterminating</b> -> symbol | symbol</code>

    NOTE the space; they must be separated by this exact structure ' -> ' and ' | '
</ul>

<p>An example for a file can be found <a href='https://github.com/w-i-l/word-in-grammar/blob/main/grammar.txt'>here</a>.</p>

<p>The <code>main.py</code> file has an instace of class <code>Grammar</code> and will run for a given word.</p>