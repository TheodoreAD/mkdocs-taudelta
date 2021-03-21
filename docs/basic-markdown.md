# Basic Markdown

## General considerations

This page contains only basic Markdown. Information on enhancements can be found in sibling pages.

The [official specification][markdown_spec] from the creator of Markdown can be found [here][markdown_spec].
A [good alternative tutorial][markdownguide_syntax] can be found [here][markdownguide_syntax].

To test official, basic Markdown syntax, one can use
[Markdown Live Preview][markdown-live-preview] which can be found [here][markdown-live-preview].

MkDocs Tau Delta is designed to avoid unnecessary complexity in writing documents,
which is why there will be no information provided regarding inline HTML.
If you decide to use it, be adivsed that some limitations apply
and consider reading the documentation above before proceeding.

A [comprehensive list of Markdown resources][awesome_markdown] can be found [here][awesome_markdown].

A [Markdown note-keeping tool][boostnote] can be found [here][boostnote].

[markdown_spec]: https://daringfireball.net/projects/markdown/syntax
[markdownguide_syntax]: https://www.markdownguide.org/basic-syntax
[markdown-live-preview]: http://markdownlivepreview.com/
[awesome_markdown]: https://github.com/mundimark/awesome-markdown
[boostnote]: https://boostnote.io/

## Headings followed by headings, surrounded by horizontal rulers

??? info "`Source Code`"
        ***

        # Heading of lines, first of its name

        ## Heading of lines, second of its name

        ### Heading of lines, third of its name

        #### Heading of lines, fourth of its name

        ##### Heading of lines, fifth of its name

        ###### Heading of lines, sixth of its name

        * * *

***

# Heading of lines, first of its name

## Heading of lines, second of its name

### Heading of lines, third of its name

#### Heading of lines, fourth of its name

##### Heading of lines, fifth of its name

###### Heading of lines, sixth of its name

* * *

## Headings followed by paragraphs, surrounded by horizontal rulers

??? info "`Source Code`"
        ---

        Heading of lines, first of its name
        ===================================

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        Heading of lines, second of its name
        ------------------------------------

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        ### Heading of lines, third of its name

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        #### Heading of lines, fourth of its name ####

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        ##### Heading of lines, fifth of its name #

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        ###### Heading of lines, sixth of its name ######

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        - - -

---

Heading of lines, first of its name
===================================

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Heading of lines, second of its name
------------------------------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

### Heading of lines, third of its name

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

#### Heading of lines, fourth of its name ####

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

##### Heading of lines, fifth of its name #

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

###### Heading of lines, sixth of its name ######

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

- - -

## Body text, inline formatting

!!! todo
    Add strikethrough and make provisions for different syntax caused by other extensions
    Try to get as close to GFM as possible

??? info "`Source Code`"
        Within body text, `inline code` is `monospaced` and *emphasized* by having a **different** `background`.
        Both types of emphasis work inside words: I*TALI*C and B**OL**D.

        `One paragraph` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

        `Still just one paragraph` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

        `First of two paragraphs` `Italic font` *Lorem ipsum dolor sit amet, consectetur adipiscing elit,
         sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.*
        `Still italic font` _Ut enim ad minim veniam, quis nostrud exercitation
         ullamco laboris nisi ut aliquip ex ea commodo consequat._

        `Second of two paragraphs` `Bold font` **Lorem ipsum dolor sit amet, consectetur adipiscing elit,
         sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.**
        `Still bold font` __Ut enim ad minim veniam, quis nostrud exercitation
         ullamco laboris nisi ut aliquip ex ea commodo consequat.__

Within body text, `inline code` is `monospaced` and *emphasized* by having a **different** `background`.
Both types of emphasis work inside words: I*TALI*C and B**OL**D.

`One paragraph` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

`Still just one paragraph` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

`First of two paragraphs` `Italic font` *Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.*
`Still italic font` _Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat._

`Second of two paragraphs` `Bold font` **Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.**
`Still bold font` __Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.__

## Unordered Lists

??? info "`Source Code`"
    ```
    A basic `unordered list` with proper indentation syntax, which allows multiple paragraphs:
    
    -   first list item
        -   first sub-list item
        -   second sub-list item
    -   *first paragraph* of second list item
        *still first paragraph* of second list item
    
        *second paragraph* of second list item
    
    -   third list item
    
    An `unordered list` with `nesting`, the lazy syntax does not allow multiple paragraphs:
    
    - Ilúvatar
    - Ainur
        - Valar
            - Melkor, the first
            - Manwë
            - Varda (Elbereth)
            - Mandos
        * Maiar
            + Úmaiar
                - Sauron
                - a Balrog
            + Istari
                - Gandalf the Grey
                - Saruman the White
    - Children of Ilúvatar
        - Elves (Firstborn)
        * Dwarves
        + Men
    
    Another `unordered list` with `nesting:`
    
    * first list item
    * second list item
      * first sublist item
      * second sublist item
        * first sub-sublist item
        * second sub-sublist item
    ```

A basic `unordered list` with proper indentation syntax, which allows multiple paragraphs:

-   first list item
    -   first sub-list item
    -   second sub-list item
-   *first paragraph* of second list item
    *still first paragraph* of second list item

    *second paragraph* of second list item

-   third list item

An `unordered list` with `nesting`, the lazy syntax does not allow multiple paragraphs:

- Ilúvatar
- Ainur
    - Valar
        - Melkor, the first
        - Manwë
        - Varda (Elbereth)
        - Mandos
    * Maiar
        + Úmaiar
            - Sauron
            - a Balrog
        + Istari
            - Gandalf the Grey
            - Saruman the White
- Children of Ilúvatar
    - Elves (Firstborn)
    * Dwarves
    + Men

Another `unordered list` with `nesting`:

* first list item
* second list item
  * first sublist item
  * second sublist item
    * first sub-sublist item
    * second sub-sublist item

!!! warning
    Indentation rules are not being observed for 2 spaces, only for 4

    Mixed - and * do not create cohesive lists

## Ordered Lists

??? info "`Source Code`"
    ```
    A basic `ordered list` with proper indentation syntax, which allows multiple paragraphs:
    
    1.  I am a winner paragraph.
        I am still a winner paragraph.
    
        I am second best paragraph.
    
    2.  Coming in second is best when there is a also...
    
    3.  ... a third
    
    An `ordered list` with `nesting`:
    
    1. first list item
    2. second list item
        1. first sub-list item
        2. second sub-list item
            1. first sub-sub-list item
            2. second sub-sub-list item
            3. third sub-sub-list item
                1. the secret fourth level of nesting
    3. third list item
        1. first sub-list item
    
    Another `ordered list` using random numbers in syntax:
    
    999. first list item
    42. second list item
    0. third list item
        5. first sub-list item
        5. second sub-list item
    
    Escape characters to avoid body text being converted into a list:
    
    > 1999\. The year before the Y2K apocalypse.
    >
    > 2020\. The year of best vision.
    >
    > \- Mark Clockworth, "The Counting of Years"
    ```

A basic `ordered list` with proper indentation syntax, which allows multiple paragraphs:

1.  I am a winner paragraph.
    I am still a winner paragraph.

    I am second best paragraph.

2.  Coming in second is best when there is a also...

3.  ... a third

An `ordered list` with `nesting`:

1. first list item
2. second list item
    1. first sub-list item
    2. second sub-list item
        1. first sub-sub-list item
        2. second sub-sub-list item
        3. third sub-sub-list item
            1. the secret fourth level of nesting
3. third list item
    1. first sub-list item

Another `ordered list` using random numbers in syntax:

999. first list item
42. second list item
0. third list item
    5. first sub-list item
    5. second sub-list item

Escape characters to avoid body text being converted into a list:

> 1999\. The year before the Y2K apocalypse.
>
> 2020\. The year of best vision.
>
> \- Mark Clockworth, "The Counting of Years"

!!! warning
    Indentation rules are not being observed for 2 spaces, only for 4

## Code blocks

??? info "`Source Code`"
    ```
    A `code block`:

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat.
    ```

A `code block`:

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

    Ut enim ad minim veniam, quis nostrud exercitation ullamco
    laboris nisi ut aliquip ex ea commodo consequat.

## Block quotes

??? info "`Source Code`"
    ```
    A `block quote` with `nesting`:

    > `First level` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    >
    >> `Second level, quote within quote` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    >
    > `Back to first level` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

    > `Still part of same block quote` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

    A `block quote` with `other Markdown elements:`

    > ### Heading ###
    >
    > Another `heading`:
    >
    > #### Heading ####
    >
    > A `text pargraph`:
    >
    > Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    >
    > An `unordered list`:
    >
    > - first list item
    >     - first sub-list item
    >     - > second sub-list item as block quote
    >
    > An `ordered list`:
    >
    > 1. first list item
    >     1. first sub-list item
    >
    > A `code block`:
    >
    >     First line of code
    >     Second line of code
    ```

A `block quote` with `nesting`:

> `First level` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
>
>> `Second level, quote within quote` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
>
> `Back to first level` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

> `Still part of same block quote` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

A `block quote` with `other Markdown elements:`

> ### Heading ###
>
> Another `heading`:
>
> #### Heading ####
>
> A `text pargraph`:
>
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
>
> An `unordered list`:
>
> - first list item
>     - first sub-list item
>     - > second sub-list item as block quote
>
> An `ordered list`:
>
> 1. first list item
>     1. first sub-list item
>
> A `code block`:
>
>     First line of code
>     Second line of code

## Tables

??? info "`Source Code`"
    ```
    Table with `alignment` and `inline formatting`:

    |    Center     | Left       |         Right |
    | :-----------: | :--------- | ------------: |
    | **Alpha One** | B1         |            C1 |
    |      A2       | *Beta Two* |            C2 |
    |      A3       | B3         | `Gamma Three` |

    Same table with `no header` and implicitly tight content wrapping:

    |               |            |               |
    | :-----------: | :--------- | ------------: |
    | **Alpha One** | B1         |            C1 |
    |      A2       | *Beta Two* |            C2 |
    |      A3       | B3         | `Gamma Three` |
    ```

Table with `alignment` and `inline formatting`:

|    Center     | Left       |         Right |
| :-----------: | :--------- | ------------: |
| **Alpha One** | B1         |            C1 |
|      A2       | *Beta Two* |            C2 |
|      A3       | B3         | `Gamma Three` |

Same table with `no header` and implicitly tight content wrapping:

|               |            |               |
| :-----------: | :--------- | ------------: |
| **Alpha One** | B1         |            C1 |
|      A2       | *Beta Two* |            C2 |
|      A3       | B3         | `Gamma Three` |

## Links

### Inline style

??? info "`Source Code`"
    ```
    Create automatic links for URLs and email addresses by surrounding the URL or email address
    with angle brackets to show the actual text of a URL or email address as a clickable link:
    
    - Click <http://example.com/> to open a browser tab.
    - Click <john.smith@example.com> to open a mail editor compose window.
    
    Refer to an online resource using the URL:
    
    - [This link](http://example.net/) has no title attribute.
    - This is [an example](http://example.com/ "Title") inline link with a title attribute.
    
    Refer to a local resource on the same server using the relative path as an URL:
    
    - See the [Enhanced Markdown](enhanced-markdown.md#inline-text-formatting) page for all fun features.
    - See the [Enhanced Markdown Inline Text Formatting](enhanced-markdown.md#inline-text-formatting) tag
      in the [Enhanced Markdown](enhanced-markdown.md#inline-text-formatting) page for a specific fun feature.
    ```

Create automatic links for URLs and email addresses by surrounding the URL or email address
with angle brackets to show the actual text of a URL or email address as a clickable link:

- Click <http://example.com/> to open a browser tab.
- Click <john.smith@example.com> to open a mail editor compose window.

Refer to an online resource using the URL:

- [This link](http://example.net/) has no title attribute.
- This is [an example](http://example.com/ "Title") inline link with a title attribute.

Refer to a local resource on the same server using the relative path as an URL:

- See the [Enhanced Markdown](enhanced-markdown.md#inline-text-formatting) page for all fun features.
- See the [Enhanced Markdown Inline Text Formatting](enhanced-markdown.md#inline-text-formatting) tag
  in the [Enhanced Markdown](enhanced-markdown.md#inline-text-formatting) page for a specific fun feature.

!!! todo "Move to Enhanced Markdown"
    `MkDocs` allows us to refer to a local resource on the same server using the relative path as an `.md` file:

    See the [Enhanced Markdown](enhanced-markdown.md) page for all the fun features.
    Specific features can't be targeted with this method because it doesn't support tags.

### Reference style

!!! todo
    Add active content

    Research the many enhancements provided by the MagicLink [extension][pymdown-magiclink].

[pymdown-magiclink]: https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/

Reference-style links use a second set of square brackets (with an optional leading space)
with a label inside that must by defined anywhere in the document on a line by itself.

    This is [an example][id] reference-style link. This is a [space-delimited example] [id].

    [id]: http://example.com/  "Optional Title Here"

The definition must contain, exactly in this order:

- square brackets containing the label (optionally left indented by up to three spaces)
- a colon
- one or more spaces
- the URL for the link
- optionally a title attribute for the link, enclosed in double quotes, single quotes or parentheses

The following three link definitions are equivalent:

    [foo]: http://example.com/  "Optional Title Here"
    [foo]: http://example.com/  'Optional Title Here'
    [foo]: http://example.com/  (Optional Title Here)

NOTE: There is a known bug in Markdown.pl 1.0.1 which prevents single quotes from being used to delimit link titles.

The link URL may, optionally, be surrounded by angle brackets:

    [id]: <http://example.com/>  "Optional Title Here"

You can put the title attribute on the next line and use extra spaces or tabs for padding,
which tends to look better with longer URLs:

    [id]: http://example.com/longish/path/to/resource/here
        "Optional Title Here"

Link definition names may consist of letters, numbers, spaces, and punctuation and are case insensitive:

    [Link text][a] and [Link text][A] are equivalent.

The `implicit link name shortcut` allows you to omit the name of the link in the second set of square brackets
and use the link text itself as the name. The link names may contain spaces.

    [Google][] and [Stack Overflow][] are a programmer's best friend.

    [Google]: https://google.com/
    [Stack Overflow]: https://stackoverflow.com/

The two examples below produce the same results:

    I get 10 times more traffic from [Google] [1] than from [Yahoo] [2] or [MSN] [3].

    [1]: http://google.com/        "Google"
    [2]: http://search.yahoo.com/  "Yahoo Search"
    [3]: http://search.msn.com/    "MSN Search"

    I get 10 times more traffic from [Google][] than from [Yahoo][] or [MSN][].

    [google]: http://google.com/        "Google"
    [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
    [msn]:    http://search.msn.com/    "MSN Search"

Link definitions are ideally placed immediately after the paragraph in which they’re used
or all at the end of your document, like footnotes.

!!! quote Philosophy
    The point of reference-style links is not that they’re easier to write.
    The point is that with reference-style links, your document source is vastly more readable.
    Compare the above examples: using reference-style links, the paragraph itself is only 81 characters long;
    with inline-style links, it’s 176 characters; and as raw HTML, it’s 234 characters.
    In the raw HTML, there’s more markup than there is text.

### Escaped characters

??? info "`Source Code`"
    ```
    Markdown provides backslash escapes for the following characters:

    - \\ backslash
    - \` backticks \`
    - \* asterisks \*
    - \_ underscores \_
    - \{ curly braces \}
    - \[ square brackets \]
    - \( parentheses \)
    - \# hash mark
    - \+ plus sign
    - \- minus sign (hyphen)
    - \. dot
    - \! exclamation mark
    ```

Markdown provides backslash escapes for the following characters:

- \\ backslash
- \` backticks
- \* asterisks \*
- \_ underscores \_
- \{ curly braces \}
- \[ square brackets \]
- \( parentheses \)
- \# hash mark
- \+ plus sign
- \- minus sign (hyphen)
- \. dot
- \! exclamation mark
