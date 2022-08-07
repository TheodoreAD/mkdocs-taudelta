# Mermaid

## What this is

[Mermaid][mermaid_docs] is a markdown-like script language for generating charts from text via javascript.

It is open source and the [repository][mermaid_repo] can be found [here][mermaid_repo].

The official [documentation site][mermaid_docs] can be found [here][mermaid_docs].

The [repository][mermaid_docs_repo] of the documentation site can be found [here][mermaid_docs_repo].

To write and preview side-by-side without a locally installed editor,
an online [live editor][mermaid-live-editor] can be found [here][mermaid-live-editor].

Visual Studio Code is a highly recommended editor for Markdown and Mermaid, and Admonition.

Usage examples and sample output are provided below.

The officially supported MkDocs Material [diagrams][mermaid_mkdocs_material] are listed [here][[mermaid_mkdocs_material].

[mermaid_repo]: https://github.com/knsv/mermaid
[mermaid_docs]: https://mermaidjs.github.io/
[mermaid_docs_repo]: https://github.com/mermaidjs/mermaid-gitbook
[mermaid-live-editor]: https://mermaidjs.github.io/mermaid-live-editor/
[mermaid_usage_flowchart]: https://mermaidjs.github.io/flowchart.html
[mermaid_usage_sequence]: https://mermaidjs.github.io/sequenceDiagram.html
[mermaid_usage_gantt]: https://mermaidjs.github.io/gantt.html
[mermaid_mkdocs_material]: https://squidfunk.github.io/mkdocs-material/reference/diagrams

## Usage

### Flowchart

More information on [usage][mermaid_usage_flowchart] can be found [here][mermaid_usage_flowchart].

??? info "`Source Code`"

    ````
    ```mermaid
    graph TD
        a --> b{To be or <br />not to be?}
        a -.-> e
        b -. not to be .-> c
        b -- to be --> d
    ```
    ````

!!! example "Output"

    ```mermaid
    graph TD
        a --> b{To be or <br />not to be?}
        a -.-> e[int32]
        b -. not to be .-> c((null))
        b -- to be --> d(zero)
    ```

### Sequence diagram

More information on [usage][mermaid_usage_sequence] can be found [here][mermaid_usage_sequence].

??? info "`Source Code`"

    ````
    ```mermaid
    sequenceDiagram
        participant Alice
        participant Bob
        Alice->John: Hello John, how are you?
        loop Healthcheck
            John->John: Fight against hypochondria
        end
        Note right of John: Rational thoughts <br/>prevail...
        John-->Alice: Great!
        John->Bob: How about you?
        Bob-->John: Jolly good!
    ```
    ````

!!! example "Output"

    ```mermaid
    sequenceDiagram
        participant Alice
        participant Bob
        Alice->John: Hello John, how are you?
        loop Healthcheck
            John->John: Fight against hypochondria
        end
        Note right of John: Rational thoughts <br/>prevail...
        John-->Alice: Great!
        John->Bob: How about you?
        Bob-->John: Jolly good!
    ```

### Class diagram

??? info "`Source Code`"

    ````
    ```mermaid
    classDiagram
    Class01 <|-- AveryLongClass : Cool
    Class03 *-- Class04
    Class05 o-- Class06
    Class07 .. Class08
    Class09 --> C2 : Where am i?
    Class09 --* C3
    Class09 --|> Class07
    Class07 : equals()
    Class07 : Object[] elementData
    Class01 : size()
    Class01 : int chimp
    Class01 : int gorilla
    Class08 <--> C2: Cool label
    ```
    ````

!!! example "Output"

    ```mermaid
    classDiagram
    Class01 <|-- AveryLongClass : Cool
    Class03 *-- Class04
    Class05 o-- Class06
    Class07 .. Class08
    Class09 --> C2 : Where am i?
    Class09 --* C3
    Class09 --|> Class07
    Class07 : equals()
    Class07 : Object[] elementData
    Class01 : size()
    Class01 : int chimp
    Class01 : int gorilla
    Class08 <--> C2: Cool label
    ```

### Entity-relationship diagrams

Simple usage:

??? info "`Source Code`"

    ````
    ```mermaid
    erDiagram
      CUSTOMER ||--o{ ORDER : places
      ORDER ||--|{ LINE-ITEM : contains
      CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
    ```
    ````

!!! example "Output"
    
    ``` mermaid
    erDiagram
      CUSTOMER ||--o{ ORDER : places
      ORDER ||--|{ LINE-ITEM : contains
      CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
    ```

Advanced usage (limited support in MkDocs Material dark themes):

??? info "`Source Code`"

    ````
    ```mermaid
    erDiagram
        CUSTOMER ||--o{ ORDER : places
        CUSTOMER {
            string name
            string custNumber
            string sector
        }
        ORDER ||--|{ LINE-ITEM : contains
        ORDER {
            int orderNumber
            string deliveryAddress
        }
        LINE-ITEM {
            string productCode
            int quantity
            float pricePerUnit
        }
    ```
    ````

!!! example "Output"

    ```mermaid
    erDiagram
        CUSTOMER ||--o{ ORDER : places
        CUSTOMER {
            string name
            string custNumber
            string sector
        }
        ORDER ||--|{ LINE-ITEM : contains
        ORDER {
            int orderNumber
            string deliveryAddress
        }
        LINE-ITEM {
            string productCode
            int quantity
            float pricePerUnit
        }
    ```

### State diagram

??? info "`Source Code`"

    ````
    ```mermaid
    stateDiagram-v2
      state fork_state <<fork>>
        [*] --> fork_state
        fork_state --> State2
        fork_state --> State3
    
        state join_state <<join>>
        State2 --> join_state
        State3 --> join_state
        join_state --> State4
        State4 --> [*]
    ```
    ````

!!! example "Output"

    ```mermaid
    stateDiagram-v2
      state fork_state <<fork>>
        [*] --> fork_state
        fork_state --> State2
        fork_state --> State3
    
        state join_state <<join>>
        State2 --> join_state
        State3 --> join_state
        join_state --> State4
        State4 --> [*]
    ```

### Gantt chart

!!! warning
    Not officially supported by MkDocs Material.

More information on [usage][mermaid_usage_gantt] can be found [here][mermaid_usage_gantt].

??? info "`Source Code`"

    ````
    ```mermaid
    gantt
    dateFormat  YYYY-MM-DD
    title Adding GANTT diagram to mermaid

    section A section
    Completed task            :done,    des1, 2014-01-06, 2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d
    ```
    ````

!!! example "Output"

    ```mermaid
    gantt
    dateFormat  YYYY-MM-DD
    title Adding GANTT diagram to mermaid

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d
    ```

### Git graph

!!! warning
    Not officially supported by MkDocs Material.
    Not supported by the currently used mermaid plugin.

The syntax allows the simulation of a sequence of Git commands.

??? note "Non-functional content"
    ??? info "`Source Code`"
    
        ````
        ```mermaid
        gitGraph:
        options
        {
            "nodeSpacing": 85,
            "nodeRadius": 5
        }
        end
        commit
        branch newbranch
        checkout newbranch
        commit
        commit
        checkout master
        commit
        commit
        merge newbranch
        commit
        ```
        ````
    
    !!! example "Output"
    
        ```mermaid
        gitGraph:
        options
        {
            "nodeSpacing": 85,
            "nodeRadius": 5
        }
        end
        commit
        branch newbranch
        checkout newbranch
        commit
        commit
        checkout master
        commit
        commit
        merge newbranch
        commit
        ```
