## Make and control Python objects from JSON or YAML files

We want to construct a hierarchical collection of Python objects from a data
file.

We will be rewriting a big Python dictionary so that we can reach all the parts
of it from the top.


# Three types of data:

* simple - strings, lists, dictionaries, booleans, `None`, numbers
* class - represents a Python class that gets constructed
* container class - a Python class that contains other class or simple data
  within it

# High-level

We have a huge dictionary.

At each level, a special member `_` has the type information - either a
typename, or the actual class.


# Details

Class data corresponds to a Python constructor.

Classes have attributes - either read-only (set in the constructor) or
read-write.

Classes have methods

A Class always has a type attribute whose name will probably be `_`.

There are potential customization points here:

These two will be classmethods:

1. pre_construction - rewrite the dictionary
2. at construction - before any child is created or public attribute is set.

-- after this step, we're an object

3. post-attribute - after all the attributes have been set
4. post-child - after all children are created
5. post-parent - after your parent has created all your siblings
6. ready - right before we're ready to start

Two different ways to construct!

1.  construct/set/init

Classes with an empty constructor, setters, and then an init() method or function

    a = Class()
    a.foo = 1
    a.bar = 'hello'
    a.init()  # or init(a)

2. Constructor-only

    a = Class(foo=1, bar='hello')

ADDRESSES!
