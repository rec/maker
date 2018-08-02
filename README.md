## Make and control Python objects from JSON or YAML files

We want to construct a hierarchical collection of Python objects from a data
file.


# Three types of data:

* simple - strings, lists, dictionaries, booleans, `None`, numbers
* class - represents a Python class that gets constructed
* container class - a Python class that contains other class data within it

Class data corresponds to a Python constructor.

Classes have attributes - either read-only (set in the constructor) or
read-write.

A Class always has a `typename` attribute

We walk the tree-depth first.

There are potential customization points at five places.

These ones will be class methods

1. pre_construction - rewrite the dictionary
2. at construction - before any child is created or public attribute is set.

-- after this, we're an object

3. post-attribute - after all the attributes have been set
4. post-child - after all children are created
5. post-parent - after your parent has created all your siblings
6. ready - right before we're ready to start
