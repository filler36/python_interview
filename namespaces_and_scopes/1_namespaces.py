"""
A namespace is a dictionary for mapping symbolic names to their values.
When you do any assignment, you are, in fact, updating a namespace dictionary.
When you refer to an object by its name, Python looks through a list of several namespaces trying to find one with the name as a key.

Since namespaces are implemented using dictionaries, you can explain why you might redefine objects.

Built-In Namespace - it does not behave like a dictionary. Python implements it as a module.
Global and Local Namespaces - these are really dictionaries for global and local namespaces. Python does implement these namespaces as dictionaries.

----------------------------------------------------------------------------------------------------------------
                         |              globals()             |                 	locals()                    |
----------------------------------------------------------------------------------------------------------------
Call location            | global variables,                  | locally defined variables,                      |
inside the function      | including a function               | input arguments for a function                  |
----------------------------------------------------------------------------------------------------------------
Call location            | global variables                   | global variables                                |
in a module level        |                                    |                                                 |
----------------------------------------------------------------------------------------------------------------
Modification possibility | yes, returns an actual reference   | no, returns only a copy of the local namespace. |
                         | to the global namespace dictionary | Thus, a change of locals() dictionary will      |
                         |                                    | not affect a real local namespace               |
----------------------------------------------------------------------------------------------------------------
"""
