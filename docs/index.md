# What is MkDocs Tau Delta?

## MkDocs

`MkDocs` is a static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

It is an open source project. Its [repository][mkdocs-repo] can be found [here][mkdocs-repo]. Its [website][mkdocs-site] can be found [here][mkdocs-site].

[mkdocs-repo]: https://github.com/mkdocs/mkdocs
[mkdocs-site]: https://www.mkdocs.org/

## MkDocs Tau Delta

`Material` is a theme for `MkDocs` built using Google's [Material Design][material-design] guidelines.

It is an open source project. Its [repository][mkdocs-material-repo] can be found [here][mkdocs-material-repo]. Its [website][mkdocs-material-site] can be found [here][mkdocs-material-site].

Other [MkDocs supported themes][mkdocs-themes-site] can be found [here][mkdocs-themes-site].

`MkDocs Tau Delta` is a modified version of the `MkDocs Material` theme.

It is an inner source project. Its [repository][mkdocs-tau-delta-repo] can be found [here][mkdocs-tau-delta-repo].

[material-design]: https://material.io/design/
[mkdocs-themes-site]: https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes
[mkdocs-material-repo]: https://github.com/squidfunk/mkdocs-material
[mkdocs-material-site]: https://squidfunk.github.io/mkdocs-material/
[mkdocs-tau-delta-repo]: https://git.csnzoo.com/tdumitrescu/mkdocs-tau-delta/

## Why "Tau Delta"

In the interest of having a proper name beyond the initials:

- `Tau` `Delta` stands for `Tremendous Documentation`
- the reasoning is that *tremendous*, as its definitions go, represents:
    - very great in amount, scale, or intensity: Tau Delta is meant for large documents
    - extremely good or impressive; excellent: Tau Delta is meant to be easy on the eyes

Philosophically:

- `T` stands for `Tight`, because font size is smaller and lines are tighter together, both in text and in tables. The pupose was to have a result closer to [Read The Docs][readthedocs] than [vanilla Material][mkdocs-material-guide].
- `D` stands for `Diverse`, because it has a number of features added, such as:
    - a plethora of [Markdown and PyMdown extensions](enhanced-markdown.md)
    - [Admonition blocks](admonition-blocks.md)
    - [GitHub emoji](emoji.md)
    - graphing via [Mermaid](mermaid.md)
    - [charting](charts.md) via [chart.js][chart-js-site.md] and [chartist.js][chartist-js-site.md] [WIP]
    - more to come!

!!! warning
    Not yet clear which parts of the [GitHub Flavored Markdown (GFM) specification][gfm-spec] work with this theme yet.

    The [PyMdown extensions site][pymdown-extensions-gfm] has a guide on how to implement GFM.

[chart-js-site]: http://www.chartjs.org/
[chartist-js-site]: https://gionkunz.github.io/chartist-js/
[readthedocs]: https://docs.readthedocs.io/en/latest/
[mkdocs-material-guide]: https://squidfunk.github.io/mkdocs-material/getting-started/
[gfm-spec]: https://github.github.com/gfm/
[pymdown-extensions-gfm]: https://facelessuser.github.io/pymdown-extensions/faq/#github-ish-configurations

## Theme setup

!!! todo
    Create an application that allows users to easily:
    * new dedicated documentation site:
        * create a skeleton for an example documentation site
        * obtain input from user: origin address including user, new repo name
        * create a new instance of MkDocs Tau Delta using a new repository
    * new documentation site as part of an ongoing project:
        * obtain input from user: repo address
        * check for existing `docs/` directory, if it already exists warn user and ask for permission to continue
        * add a new instance of MkDocs Tau Delta to an existing repository
    * existing documentation site:
        * check for existence of `mkdocs.yml` and `docs/extra.css`
        * get the latest `extra.css` and `mkdocs.yml` from the MkDocs Tau Delta repo
        * update local `extra.css` and the extensions section of `mkdocs.yml` with the latest content

### Configuration files

The following components are customized and are the only files you need to include to have the docs site up and running:

- mandatory:
    - `mkdocs.yml` file for most site settings in `/` (root)
    - `extra.css` for font size and spacing settings in `/docs/`
    - `gilab-ci.yml` for autoloading in GitLab in `/` (root)
- optional:
    - `favicon.ico` in `/docs/img/`
    - `logo.svg` in `/docs/img/`

By adding the files above to your repo, `https://git.csnzoo.com/USER/REPO/`, the site should become available at `https://docs.csnzoo.com/USER/REPO/`.

A local article on [how to make your own favicon.ico and logo.svg](favicon-and-logo.md) can be found [here](favicon-and-logo.md).

### Colors

Primary color is used for top bar and hyperlinks. It is set `primary: 'blue'`. The default `indigo` was replaced with `blue` for better visibility of inline hyperlinks, `blue` vs `black` is better than `indigo` vs `black`.

Accent color is used for hyperlinks on hover. It is set `accent: 'blue'`. The default `indigo` was replaced with `orange` for better visibility of hyperlinks on hover, and is also a good choice if the primary color is restored to `indigo`.

The options for can be found in the table below. They have been compiled from [here][mkdocs-yml-theme-color-primary] for [primary colors][mkdocs-yml-theme-color-primary] and from [here][mkdocs-yml-theme-color-accent] for [accent colors][mkdocs-yml-theme-color-accent].

| mkdocs.yml  | scss                  | primary | accent |
| ----------- | --------------------- | :-----: | :----: |
| red         | $clr-red-a400         |    X    |   X    |
| pink        | $clr-pink-a400        |    X    |   X    |
| purple      | $clr-purple-a200      |    X    |   X    |
| deep-purple | $clr-deep-purple-a200 |    X    |   X    |
| indigo      | $clr-indigo-a200      |    X    |   X    |
| blue        | $clr-blue-a200        |    X    |   X    |
| light-blue  | $clr-light-blue-a700  |    X    |   X    |
| cyan        | $clr-cyan-a700        |    X    |   X    |
| teal        | $clr-teal-a700        |    X    |   X    |
| green       | $clr-green-a700       |    X    |   X    |
| light-green | $clr-light-green-a700 |    X    |   X    |
| lime        | $clr-lime-a700        |    X    |   X    |
| yellow      | $clr-yellow-a700      |    X    |   X    |
| amber       | $clr-amber-a700       |    X    |   X    |
| orange      | $clr-orange-a400      |    X    |   X    |
| deep-orange | $clr-deep-orange-a200 |    X    |   X    |
| brown       | $clr-brown-500        |    X    |        |
| grey        | $clr-grey-600         |    X    |        |
| blue-grey   | $clr-blue-grey-600    |    X    |        |

[mkdocs-yml-theme-color-primary]: https://github.com/squidfunk/mkdocs-material/blob/master/src/assets/stylesheets/application-palette.scss#L65
[mkdocs-yml-theme-color-accent]: https://github.com/squidfunk/mkdocs-material/blob/master/src/assets/stylesheets/application-palette.scss#L229
