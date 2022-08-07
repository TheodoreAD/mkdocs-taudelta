# Live Editor

## What this is

### Philosophy

The point of `MkDocs Tau Delta` is to make `Markdown` the language of choice
among engineers writing documentation.

An additional goal is to address a larger group of users
beyond the ones creating documentation.
If meeting minutes, roadmaps, speeches, presentation notes could be created
on-the-fly and saved to a site where stakeholders can read and contribute
to the documents easily, then senior engineers, team leads and
project/product/department managers would become part of the target audience,
leading to significantly increased product proliferation.

Success depends on at least four factors:

- richness of features
- quality, both functionally and aesthetically
- ease of setup
- ease of use

This section is an attempt to improve the ease of use through the cunning use
of a free live editor, which is naturally not a part of the project.

### Requirements

The ideal set of features is:

- edit Markdown documents in a `free`, `ad-free`, `clutter-free` split-screen editor and preview web app
- open Markdown documents directly from an MkDocs Tau Delta enabled repository
- save Markdown documents directly to an MkDocs Tau Delta enabled repository
- continuously synchronize with the persistent document source while editing

This would enable the use of Markdown for note-taking as well as for documentation.

## Proposed software

### StackEdit

StackEdit is a full-featured, open-source Markdown editor based on PageDown,
the Markdown library used by Stack Overflow and the other Stack Exchange sites.

It is an open source project. Its [repository][stackedit-repo] can be found [here][stackedit-repo].
Its [web application][stackedit-app] can be found [here][stackedit-app].

[stackedit-repo]: https://github.com/benweet/stackedit
[stackedit-app]: https://stackedit.io/app

### Dillinger

Dillinger is a cloud-enabled, mobile-ready, offline-storage, AngularJS powered HTML5 Markdown editor.

It is an open source project. Its [repository][dillinger-repo] can be found [here][dillinger-repo].
Its [web application][dillinger-app] can be found [here][dillinger-app].

[dillinger-repo]: https://github.com/joemccann/dillinger
[dillinger-app]: https://dillinger.io/

!!! todo
    Test integration and synchronization with `Google Drive` and `GitHub`.

    Explore viability of connection with GitLab.

## Converting existing HTML content to Markdown

### Pandoc

Pandoc is a Haskell library for converting from one markup format to another,
and a command-line tool that uses this library.

It is an open source project. Its [repository][pandoc-repo] can be found [here][pandoc-repo].
Its [web application][pandoc-app] can be found [here][pandoc-app].
Its [website][pandoc-site] can be found [here][pandoc-site].

[pandoc-site]: https://pandoc.org/index.html
[pandoc-repo]: https://github.com/jgm/pandoc
[pandoc-app]: https://pandoc.org/try/?text=SampleTextString&from=html&to=markdown

### Turndown

Turndown is an HTML to Markdown converter written in JavaScript.

It is an open source project. Its [repository][turndown-repo] can be found [here][turndown-repo].
Its [web application][turndown-app] can be found [here][turndown-app].

It also has a [GitHub Flavored Markdown plugin][turndown-gfm-plugin-repo]
that can be found [here][turndown-gfm-plugin-repo].

[turndown-repo]: https://github.com/domchristie/turndown
[turndown-app]: http://domchristie.github.io/turndown/
[turndown-gfm-plugin-repo]: https://github.com/domchristie/turndown-plugin-gfm

## WordPress theme with Markdown support

### Jetpack

From the [website][jetpack-site]:

> Browse hundreds of professionally-designed WordPress themes to find the right one for your site.
>
> Customize your homepage, blog posts, sidebars, and widgets — all without touching any code.
>
> Seamlessly embed rich content and videos, deliver them all at high speed, and replace default search with an Elasticsearch-powered service.

An article about [Markdown support][jetpack-site-markdown] can be found [here][jetpack-site-markdown].

[jetpack-site]: https://jetpack.com/
[jetpack-site-markdown]: https://jetpack.com/support/markdown/
