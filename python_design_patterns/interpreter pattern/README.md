The interpreter pattern is related only to internal DSLs. Therefore, our goal is to create a
simple but useful language using the features provided by the host programming language,
which in this case is Python. Note that Interpreter does not address parsing at all. It
assumes that we already have the parsed data in some convenient form. This can be an
abstract syntax tree (AST) or any other handy data structure.


The Interpreter pattern is used when we want to offer a simple language to domain experts
and advanced users to solve their problems. The first thing we should stress is that the
interpreter should only be used to implement simple languages. If the language has the
requirements of an external DSL, there are better tools to create languages from scratch
(Yacc and Lex, Bison, ANTLR, and so on).


Our goal is to offer the right programming abstractions to the specialist, who is often not a
programmer, to make them productive. Ideally, they shouldn't know advanced Python to
use our DSL, but knowing even a little bit of Python is a plus since that's what we
eventually get at the end. Advanced Python concepts should not be a requirement.
Moreover, the performance of the DSL is usually not an important concern. The focus is on
offering a language that hides the peculiarities of the host language and offers a more
human-readable syntax. Admittedly, Python is already a very readable language with far
less peculiar syntax than many other programming languages.