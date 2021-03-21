# Enhanced Markdown

Extension sources:

- `Markdown` extension [documentation][markdown-extensions-site]
- `PyMdown` extension [documentation][pymdown-extensions-site], [repository][pymdown-extensions-repo]
  and [related MkDocs documentation][mkdocs-pymdown-extensions-site]
- test `.md` file from the `PyMdown` [repository][md-example-pymdown]
- example `mkdocs.yml` files from the `PyMdown` [repository][mkdocs-yml-example-pymdown]
  and the `pymdown-extensions` [repository][mkdocs-yml-example-pymdown-extesnions]

[markdown-extensions-site]: https://python-markdown.github.io/extensions/
[pymdown-extensions-site]: https://facelessuser.github.io/pymdown-extensions/
[pymdown-extensions-repo]: https://github.com/facelessuser/pymdown-extensions
[mkdocs-pymdown-extensions-site]: https://squidfunk.github.io/mkdocs-material/extensions/pymdown/
[md-example-pymdown]: https://github.com/facelessuser/PyMdown/blob/master/examples/example.md
[mkdocs-yml-example-pymdown]: https://github.com/facelessuser/PyMdown/blob/master/mkdocs.yml
[mkdocs-yml-example-pymdown-extesnions]: https://github.com/facelessuser/pymdown-extensions/blob/master/mkdocs.yml

Planned features:

- [SaneLists][markdown-sanelists]
- [NewLineToBreak][markdown-nl2br] (CAUTION: major deviation from basic Markdown)
- [Critic][pymdown-critic]
- [MagicLink][pymdown-magiclink]
- [Snippets][pymdown-snippets] (HIGH PRIORITY)
- [Arithmatex][pymdown-arithmatex]
- [BetterEm][pymdown-betterem] (CAUTION: deviation from basic Markdown)
- [EscapeAll][pymdown-escapeall]

[markdown-sanelists]: https://python-markdown.github.io/extensions/sane_lists/
[markdown-nl2br]: https://python-markdown.github.io/extensions/nl2br
[pymdown-critic]: https://facelessuser.github.io/pymdown-extensions/extensions/critic/
[pymdown-magiclink]: https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/
[pymdown-snippets]: https://facelessuser.github.io/pymdown-extensions/extensions/snippets/
[pymdown-arithmatex]: https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/
[pymdown-betterem]: https://facelessuser.github.io/pymdown-extensions/extensions/betterem/
[pymdown-escapeall]: https://facelessuser.github.io/pymdown-extensions/extensions/escapeall/

## Inline text formatting

### Emphasis

Uses the `PyMdown Caret` [extension][pymdown-caret] and the `PyMdown Tilde` [extension][pymdown-tilde].

??? info "`Source code`"
    ```
    - inserted text is displayed as ^^underlined^^ and has the `<ins>` HTML tag
    - deleted text is displayed as ~~strikethrough~~ and has the `<del>` HTML tag
    ```

- inserted text is displayed as ^^underlined^^ and has the `<ins>` HTML tag
- deleted text is displayed as ~~strikethrough~~ and has the `<del>` HTML tag

### Subscript and Superscript

Uses the `PyMdown Caret` [extension][pymdown-caret]
and the `PyMdown Tilde` [extension][pymdown-tilde] (syntax follows Pandoc style).

[pymdown-caret]: https://facelessuser.github.io/pymdown-extensions/extensions/caret/
[pymdown-tilde]: https://facelessuser.github.io/pymdown-extensions/extensions/tilde/

??? info "`Source Code`"
    ```
    - chemistry is fun: CH~3~CH~2~OH [ClO~2~]^+^
    - math is fun (even without [LaTeX][pymdown-arithmatex]): x^2^ + y^2^ = 4; a~1~ + a~2~ + ... + a~n-1~ = a~n~
    - math is beautiful: e^i\ ·\ π^ + 1 = 0
    - superscript^with spaces won't work^, but superscript^\ with\ escaped\ spaces\ will\ work^
    - subscript~with spaces won't work~ but subscript~\ with\ escaped\ spaces\ will\ work~
    ```

- chemistry is fun: CH~3~CH~2~OH [ClO~2~]^+^
- math is fun (even without [LaTeX][pymdown-arithmatex]): x^2^ + y^2^ = 4; a~1~ + a~2~ + ... + a~n-1~ = a~n~
- math is beautiful: e^i\ ·\ π^ + 1 = 0
- superscript^with spaces won't work^, but superscript^\ with\ escaped\ spaces\ will\ work^
- subscript~with spaces won't work~ but subscript~\ with\ escaped\ spaces\ will\ work~

### Highlighting

Uses the `PyMdown Mark` [extension][pymdown-mark].

[pymdown-mark]: https://facelessuser.github.io/pymdown-extensions/extensions/mark/

??? info "`Source Code`"
    ```
    - someone is `highlighting` random ==bits== of ==text== all ==over== the place
    - marking is smart even when its markers are ==used==inside==a==sentence==
    ```

- someone is `highlighting` random ==bits== of ==text== all ==over== the place
- marking is smart even when its markers are ==used==inside==a==sentence==

## Special characters

Uses the `Smarty` [extension][markdown-smarty].

[markdown-smarty]: https://python-markdown.github.io/extensions/smarty/

??? info "`Source Code`"
    ```
    - 'a `left-single-quote` to the left and a `right-single-quote` to the right'
    - "a `left-double-quote` to the left and a `right-double-quote` to the right"
    - `[DISABLED]` `<<`a `left-angle-quote` to the left and a `right-angle-quote` to the right`>>`
    - an `ellipsis` at the very end...
    - an `ndash` is longer than -- say -- a `hyphen`
    - an `mdash` is longer than --- say --- an `ndash`
    ```

- 'a `left-single-quote` to the left and a `right-single-quote` to the right'
- "a `left-double-quote` to the left and a `right-double-quote` to the right"
- `[DISABLED]` `<<`a `left-angle-quote` to the left and a `right-angle-quote` to the right`>>`
- an `ellipsis` at the very end...
- an `ndash` is longer than -- say -- a `hyphen`
- an `mdash` is longer than --- say --- an `ndash`

***

Uses the `PyMdown Smart Symbols` [extension][pymdown-smartsymbols].

[pymdown-smartsymbols]: https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/

??? info "`Source Code`"
    ```
    - this creative work is `Copyright` (c) `Trademark` (tm) `Registered` (r) and free to reproduce
    - to direct mail to an addressee not at the usual place of receipt, use the `care of` notation c/o
    - with things being `not equal,` X =/= Y, things are something `plus or minus` another thing, X = Y +/- Z
    - a `right arrow` --> points to a `double arrow` <--> which also points to a `left arrow` <--
    - `fractions` galore: 1/2 1/4 3/4 1/3 2/3 1/5 2/5 3/5 4/5 1/6 5/6 1/8 3/8 5/8 7/8
    - `ordinals` galore: 1st 2nd 3rd 4th 5th 10th; 1,000th 1,000th and bazillionth doesn't work
    ```

- this creative work is `Copyright` (c) `Trademark` (tm) `Registered` (r) and free to reproduce
- to direct mail to an addressee not at the usual place of receipt, use the `care of` notation c/o
- with things being `not equal,` X =/= Y, things are something `plus or minus` another thing, X = Y +/- Z
- a `right arrow` --> points to a `double arrow` <--> which also points to a `left arrow` <--
- `fractions` galore: 1/2 1/4 3/4 1/3 2/3 1/5 2/5 3/5 4/5 1/6 5/6 1/8 3/8 5/8 7/8
- `ordinals` galore: 1st 2nd 3rd 4th 5th 10th; 1,000th 1,000th and bazillionth doesn't work

## Keyboard keys

Uses the `PyMdown Keys` [extension][pymdown-keys].

[pymdown-keys]: https://facelessuser.github.io/pymdown-extensions/extensions/keys/

!!! TODO
    Fix glyphs being too low in keys.

??? info "`Source code`"
    ```
    - Windows: ++ctrl+alt+delete++
    - Office: ++ctrl+c++ ++ctrl+v++
    - Mac: ++cmd++
    - Media: ++media++ ++a++ ++d++ ++s++ ++ctrl++ ++y++ ++o++ ++u++
    - Star Trek: ++space++ ++end++
    - wrong command: ++ctrl++ ++break++ ++reset++
    ```

- Windows: ++ctrl+alt+delete++
- Office: ++ctrl+c++ ++ctrl+v++
- Mac: ++cmd++
- Media: ++media++ ++a++ ++d++ ++s++ ++ctrl++ ++y++ ++o++ ++u++
- Star Trek: ++space++ ++end++
- wrong command: ++ctrl++ ++break++ ++reset++

## Checklists

Uses the `Pymdown Tasklist` [extension][pymdown-tasklist].

[pymdown-tasklist]: https://facelessuser.github.io/pymdown-extensions/extensions/tasklist/

!!! TODO
    Fix checkboxes being too low.

??? info "`Source code`"
    ```
    A `checklist` with `nesting`:
    
    - [x] checked item
    - [ ] unchecked item
        - [ ] unchecked sub-item
        - [x] checked sub-item
            - [ ] unchecked sub-sub-item
            - [x] checked sub-sub-item
        - [ ] unchecked sub-item
    - [ ] unchecked item
    
    Another `checklist` with `nesting`:
    
    - [x] checked item
      - [ ] unchecked sub-item
        - [x] checked sub-sub-item
      - [ ] unchecked sub-item
    - [x] checked item
    ```

A `checklist` with `nesting`:

- [x] checked item
- [ ] unchecked item
    - [ ] unchecked sub-item
    - [x] checked sub-item
        - [ ] unchecked sub-sub-item
        - [x] checked sub-sub-item
    - [ ] unchecked sub-item
- [ ] unchecked item

A `checklist` with `nesting` inside Admonition block:

!!! note
    - [x] checked item
      - [ ] unchecked sub-item
        - [x] checked sub-sub-item
      - [ ] unchecked sub-item
    - [x] checked item

## Abbreviations and Definition Lists

Uses the `Abbreviations` [extension][markdown-abbreviations].

[markdown-abbreviations]: https://python-markdown.github.io/extensions/abbreviations/

??? info "`Source code`"
    ```
    Bewildering *[abbreviations][abbreviation-disambiguation]* such as Mssr. and its jocund plural, Mssrs.,
    *[initialisms][abbreviation-disambiguation]* such as PHP or
    *[acronyms][abbreviation-disambiguation]* such as ATLAS, LISP and FORTRAN
    can be defined and end up inside `<abbr>` tags.

    *[Mssr]: Monsieur
    *[Mssrs]: Messieurs
    *[PHP]: "Personal Home Page" and later the recursive acronym "PHP: Hypertext Preprocessor"
    *[ATLAS]: "A Toroidal LHC ApparatuS": one of the seven particle detector experiments constructed at the LHC (Large Hadron Collider), a particle accelerator at CERN (the European Organization for Nuclear Research) in Switzerland
    ```

Bewildering *[abbreviations][abbreviation-disambiguation]* such as Mssr. and its jocund plural, Mssrs.,
*[initialisms][abbreviation-disambiguation]* such as PHP or
*[acronyms][abbreviation-disambiguation]* such as ATLAS, LISP and FORTRAN
can be defined and end up inside `<abbr>` tags.

*[Mssr]: Monsieur
*[Mssrs]: Messieurs
*[PHP]: "Personal Home Page" and later the recursive acronym "PHP: Hypertext Preprocessor"
*[LISP]: LISt Processor
*[FORTRAN]: FORmula TRANslation
*[ATLAS]: "A Toroidal LHC ApparatuS": one of the seven particle detector experiments constructed at the LHC (Large Hadron Collider), a particle accelerator at CERN (the European Organization for Nuclear Research) in Switzerland

[abbreviation-disambiguation]: http://acronym-guide.com/difference-between-acronyms-and-abbreviations.html

***

Uses the `DefinitionLists` [extension][markdown-definition-lists].

[markdown-definition-lists]: https://python-markdown.github.io/extensions/definition_lists/

??? info "`Source code`"
    ```
    LISP
    :   A family of computer programming languages with a long history and a distinctive,
        fully parenthesized prefix notation. Originally specified in 1958, LISP is
        the second-oldest high-level programming language in widespread use today.
        Only Fortran is older, by one year.
    
        `#!lisp (apply 'append (mapcar '(lambda ( x ) (list (car x) (cadr x) (cons 40 swd) (cons 41 (setq swd (+ swd (* del (/ (caddr x) len))))))) lst))`
    
    FORTRAN
    :   A general-purpose, compiled imperative programming language
        that is especially suited to numeric computation and scientific computing.
    
        > People are very flexible and learn to adjust to strange surroundings — they can
        > become accustomed to read Lisp and Fortran programs, for example.
        >
        > Leon Sterling and Ehud Shapiro, Art of PROLOG, MIT Press.
    
    PHP
    :   A language with many magical features
        and no architect.
    
        This has never deterred the masses to adopt and its creators improve the language.
    
        > I did not develop the PHP we know today. Dozens, if not hundreds of people, developed PHP.
        > I was simply the first developer.
        >
        > I don't know how to stop it, there was never any intent to write a programming language [...]
        > I have absolutely no idea how to write a programming language, I just kept adding the next logical step on the way.
        >
        > Rasmus Lerdorf
    ```

LISP
:   A family of computer programming languages with a long history and a distinctive,
    fully parenthesized prefix notation. Originally specified in 1958, LISP is
    the second-oldest high-level programming language in widespread use today.
    Only Fortran is older, by one year.

    `#!lisp (apply 'append (mapcar '(lambda ( x ) (list (car x) (cadr x) (cons 40 swd) (cons 41 (setq swd (+ swd (* del (/ (caddr x) len))))))) lst))`

FORTRAN
:   A general-purpose, compiled imperative programming language
    that is especially suited to numeric computation and scientific computing.

    > People are very flexible and learn to adjust to strange surroundings — they can
    > become accustomed to read Lisp and Fortran programs, for example.
    >
    > Leon Sterling and Ehud Shapiro, Art of PROLOG, MIT Press.

PHP
:   A language with many magical features
    and no architect.

    This has never deterred the masses to adopt and its creators improve the language.

    > I did not develop the PHP we know today. Dozens, if not hundreds of people, developed PHP.
    > I was simply the first developer.
    >
    > I don't know how to stop it, there was never any intent to write a programming language [...]
    > I have absolutely no idea how to write a programming language, I just kept adding the next logical step on the way.
    >
    > Rasmus Lerdorf

## Footnotes

Uses the `Footnotes` [extension][markdown-footnotes].

[markdown-footnotes]: https://python-markdown.github.io/extensions/footnotes/

??? info "`Source code`"
    ```
    Footnotes[^1] have a label[^label-footnote] and content.
    They are numbered automatically regardless of label[^third-footnote].

    [^1]: This is the first footnote.
    [^label-footnote]: This is the footnote with the label `[^label-footnote]`. Mind the carrot (read caret).
    [^third-footnote]:
        This is the third and final footnote. This is its *first* paragraph.

        It is preceded by `3.` even though its label is `[^third-footnote]`.
        This is its *second* paragraph.

        > Fascinating facts may be found
        > quoted within a `blockquote.`

            code has been recorded to live inside footnotes

        The end of the **Third Age.**
    ```

Footnotes[^1] have a label[^label-footnote] and content.
They are numbered automatically regardless of label[^third-footnote].

[^1]: This is the first footnote.
[^label-footnote]: This is the footnote with the label `[^label-footnote]`. Mind the carrot (read caret).
[^third-footnote]:
    This is the third and final footnote. This is its *first* paragraph.

    It is preceded by `3.` even though its label is `[^third-footnote]`.
    This is its *second* paragraph.

    > Fascinating facts may be found
    > quoted within a `blockquote.`

        code has been recorded to live inside footnotes

    The end of the **Third Age.**

## Progress Bars

Uses the `Pymdown ProgressBar` [extension][pymdown-progressbar].

[pymdown-progressbar]: https://facelessuser.github.io/pymdown-extensions/extensions/progressbar/

??? info "`Source code`"
    ```
    | Test                | Result                                     |
    | ------------------- | ------------------------------------------ |
    | Animated: 0%        | [=0% "0%"]{: .candystripe-animate}         |
    | Animated: 5%        | [=5% "5%"]{: .candystripe-animate}         |
    | Animated: 25%       | [=25% "25%"]{: .candystripe-animate}       |
    | Animated: 45%       | [=45% "45%"]{: .candystripe-animate}       |
    | Animated: 65%       | [=65% "65%"]{: .candystripe-animate}       |
    | Animated: 85%       | [=85% "85%"]{: .candystripe-animate}       |
    | Animated: 100%      | [=100% "100%"]{: .candystripe-animate}     |
    | Division Percentage | [= 212.2/537 "212.2/537 Testing division"] |
    | No Label            | [= 50%]                                    |
    | Inline              | Before[= 50% "I'm a block!"]After          |
    ```

!!! error
    not working despite extension being enabled and the HTML being produced correctly

| Test                | Result                                     |
| ------------------- | ------------------------------------------ |
| Animated: 0%        | [=0% "0%"]{: .candystripe-animate}         |
| Animated: 5%        | [=5% "5%"]{: .candystripe-animate}         |
| Animated: 25%       | [=25% "25%"]{: .candystripe-animate}       |
| Animated: 45%       | [=45% "45%"]{: .candystripe-animate}       |
| Animated: 65%       | [=65% "65%"]{: .candystripe-animate}       |
| Animated: 85%       | [=85% "85%"]{: .candystripe-animate}       |
| Animated: 100%      | [=100% "100%"]{: .candystripe-animate}     |
| Division Percentage | [= 212.2/537 "212.2/537 Testing division"] |
| No Label            | [= 50%]                                    |
| Inline              | Before[= 50% "I'm a block!"]After          |
