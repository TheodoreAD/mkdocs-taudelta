# Admonition Blocks

Uses the `Admonition` [extension][markdown-admonition].

[markdown-admonition]: https://squidfunk.github.io/mkdocs-material/extensions/admonition/

!!! todo
    find a way to have notes without title but with an icon on a colored background on the left of the text box instead of on the top

    a good example is another MkDocs theme that can be found at:

    <https://yakworks.github.io/mkdocs-material-components/blocks/#examples>

## Basic usage

### General note

> ??? info "`Source Code`"
>     ```
>     !!! note
>         meow
>
>     !!! seealso
>     ```

***

!!! note
    meow

!!! seealso

### No title & custom title (applies to all blocks)

> ??? info "`Source Code`"
>     ```
>     !!! note ""
>         I am no one. I have no title.
>
>     !!! note "This is my personal note"
>         This note is unlike most other notes because it has a custom title.
>     ```

***

!!! note ""
    I am no one. I have no title.

!!! note "This is my personal note"
    This note is unlike most other notes because it has a custom title.

### Abstract, Information, Tip

> ??? info "`Source Code`"
>     ```
>     !!! abstract
>         woof
>
>     !!! summary
>
>     !!! tldr
>
>     !!! info
>         meow...
>
>     !!! todo
>
>     !!! tip
>         woof
>
>     !!! hint
>
>     !!! important
>     ```

***

!!! abstract
    woof

!!! summary

!!! tldr

!!! info
    meow...

!!! todo

!!! tip
    woof

!!! hint

!!! important

### Success, Failure

> ??? info "`Source Code`"
>     ```
>     !!! success
>         meow!
>
>     !!! check
>
>     !!! done
>
>     !!! failure
>         woof... woof.
>
>     !!! fail
>
>     !!! missing
>     ```

***

!!! success
    meow!

!!! check

!!! done

!!! failure
    woof... woof.

!!! fail

!!! missing

### Warning, Danger, Bug

> ??? info "`Source Code`"
>     ```
>     !!! warning
>         woof!
>
>     !!! caution
>
>     !!! attention
>
>     !!! danger
>         woof! woof!
>
>     !!! error
>
>     !!! bug
>         woof...
>     ```

***

!!! warning
    woof!

!!! caution

!!! attention

!!! danger
    woof! woof!

!!! error

!!! bug
    woof...

### Question, Example, Quote

> ??? info "`Source Code`"
>     ```
>     !!! question
>         meow?
>
>     !!! help
>
>     !!! faq
>
>     !!! example
>         meow, meow, meow.
>
>     !!! snippet
>         mw
>
>     !!! quote
>         woof woof, woof, woof.
>
>     !!! cite
>     ```

***

!!! question
    meow?

!!! help

!!! faq

!!! example
    meow, meow, meow.

!!! snippet
    mw

>>!!! error
    snippet not displaying the same icon as example

!!! quote
    woof woof, woof, woof.

!!! cite

## Combined usage

### Collapsible (applies to all blocks)

> ??? info "`Source Code`"
>     ```
>     ??? tip "Collapsible block"
>         Collapsible content initially hidden
>
>     ???+ warning "Collapsible block"
>         Collapsible content initially shown
>
>     ??? tip "Empty collapsible block, initially collapsed"
>
>     ???+ warning "Empty collapsible block, initially expanded"
>     ```

***

??? tip "Collapsible block"
    Collapsible content initially hidden

???+ warning "Collapsible block"
    Collapsible content initially shown

??? tip "Empty collapsible block, initially collapsed"

???+ warning "Empty collapsible block, initially expanded"

### Nested

> ??? info "`Source Code`"
>     ```
>     !!! quote "Ancient"
>         "I am Ozymandias, King of Kings.
>
>         !!! quote "Egypt"
>             If any want to know how great I am and where I lie,
>
>             !!! quote "Nile"
>                 let him outdo me in my work."
>     ```

***

!!! quote "Ancient"
    "I am Ozymandias, King of Kings.

    !!! quote "Egypt"
        If any want to know how great I am and where I lie,

        !!! quote "Nile"
            let him outdo me in my work."

### With code block as content

> ??? info "`Source Code`"
>     ```
>     !!! example
>         Using the powerful `Superfences` [extension][pymdown-superfences] to render code blocks here:
>
>         ```php hl_lines="3 5" linenums="24"
>         function human_test() {
>             if empty($soul) {
>                 return 'php';
>             } else {
>                 return 'kitty';
>             }
>         }
>         ```
>     ```

***

!!! example
    Using the powerful `Superfences` [extension][pymdown-superfences] to render code blocks here:

    ```php hl_lines="3 5" linenums="24"
    function human_test() {
        if empty($soul) {
            return 'php';
        } else {
            return 'kitty';
        }
    }
    ```

[pymdown-superfences]: https://facelessuser.github.io/pymdown-extensions/extensions/superfences/

### With table as content

> ??? info "`Source Code`"
>     ```
>     !!! example
>         | Center    | Left     | Right       |
>         | :-------: | :------- | ----------: |
>         | Alpha One | B1       | C1          |
>         | A2        | Beta Two | C2          |
>         | A3        | B3       | Gamma Three |
>     ```

***

!!! example
    | Center    | Left     | Right       |
    | :-------: | :------- | ----------: |
    | Alpha One | B1       | C1          |
    | A2        | Beta Two | C2          |
    | A3        | B3       | Gamma Three |
