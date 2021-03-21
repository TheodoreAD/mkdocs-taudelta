# Enhanced Markdown Code

## Inline code

### Regular inline code

??? info "`Source Code`"
    ```
    This code `function human_test() { if empty($soul) { return 'php'; } else { return 'kitty'; } }` is PHP.
    No language has been delcared.
    ```

This code `function human_test() { if empty($soul) { return 'php'; } else { return 'kitty'; } }` is PHP.

### Highlighted inline code

Uses the `Pymdown InlineHilite` [extension][pymdown-inlinehilite]
and the `Pymdown Highlight` [extension][pymdown-highlight].

[pymdown-inlinehilite]: https://facelessuser.github.io/pymdown-extensions/extensions/inlinehilite/
[pymdown-highlight]: https://facelessuser.github.io/pymdown-extensions/extensions/highlight/

??? info "`Source Code`"
    ```
    This code `#!php function human_test() { if empty($soul) { return 'php'; } else { return 'kitty'; } }` is PHP.
    It's regular inline code that beings with a shebang (or hashbang, for sticklers) and the language, e.g. `#!php`.
    ```

This code `#!php function human_test() { if empty($soul) { return 'php'; } else { return 'kitty'; } }` is PHP.
It's regular inline code that beings with a shebang (or hashbang, for sticklers) and the language, e.g. `#!php`.

## Code blocks

### Regular (no language declared)

Uses the `Pymdown Highlight` [extension][pymdown-highlight].

??? info "`Source Code`"
    ````
    ```
    function human_test() {
        if empty($soul) {
            return 'php';
        } else {
            return 'kitty';
        }
    }
    ```
    ````

```
function human_test() {
    if empty($soul) {
        return 'php';
    } else {
        return 'kitty';
    }
}
```

### With syntax highlighting (language declared)

Uses the `Pymdown SuperFences` [extension][pymdown-superfences]
and the `Pymdown Highlight` [extension][pymdown-highlight].

[pymdown-superfences]: https://facelessuser.github.io/pymdown-extensions/extensions/superfences/

??? info "`Source Code`"
    ````
    ```php
    function human_test() {
        if empty($soul) {
            return 'php';
        } else {
            return 'kitty';
        }
    }
    ```
    ````

```php
function human_test() {
    if empty($soul) {
        return 'php';
    } else {
        return 'kitty';
    }
}
```

### With syntax highlighting, code line highlighting and line numbers

Uses the `Pymdown SuperFences` [extension][pymdown-superfences]
and the `Pymdown Highlight` [extension][pymdown-highlight].

#### Regular

??? info "`Source Code`"
    ````
    ```php hl_lines="3 5" linenums="1 2 2"
    function human_test() {
        if empty($soul) {
            return 'php';
        } else {
            return 'kitty';
        }
    }
    ```
    ````

```php hl_lines="3 5" linenums="1 2 2"
function human_test() {
    if empty($soul) {
        return 'php';
    } else {
        return 'kitty';
    }
}
```

#### Inside Admonition block

??? info "`Source Code`"
    ````
    !!! note "Code block"
        Uses the superfences extension to render code blocks here:

        ```php hl_lines="3 5" linenums="24"
        function human_test() {
            if empty($soul) {
                return 'php';
            } else {
                return 'kitty';
            }
        }
        ```
    ````

!!! note "Code block"
    Uses the superfences extension to render code blocks here:

    ```php hl_lines="3 5" linenums="24"
    function human_test() {
        if empty($soul) {
            return 'php';
        } else {
            return 'kitty';
        }
    }
    ```

### Tabbed code blocks

Uses the `Pymdown SuperFences` [extension][pymdown-superfences]
and the `Pymdown Highlight` [extension][pymdown-highlight].

??? info "`Source Code`"
    ````
    === "Bash"
    
        ``` bash
        #!/bin/bash
        
        echo "Hello world!"
        ```
    
    === "C"
    
        ``` c
        #include <stdio.h>
        
        int main(void) {
          printf("Hello world!\n");
        }
        ```
    
    === "C++"
    
        ``` c++
        #include <iostream>
        
        int main() {
          std::cout << "Hello world!" << std::endl;
          return 0;
        }
        ```
    
    === "C#"
    
        ``` c#
        using System;
        
        class Program {
          static void Main(string[] args) {
            Console.WriteLine("Hello world!");
          }
        }
        ```
    ````

=== "Bash"

    ``` bash
    #!/bin/bash
    
    echo "Hello world!"
    ```

=== "C"

    ``` c
    #include <stdio.h>
    
    int main(void) {
      printf("Hello world!\n");
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>
    
    int main() {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

=== "C#"

    ``` c#
    using System;
    
    class Program {
      static void Main(string[] args) {
        Console.WriteLine("Hello world!");
      }
    }
    ```
