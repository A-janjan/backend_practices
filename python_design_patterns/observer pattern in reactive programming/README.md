# The Observer Pattern in Reactive Programming


the Observer pattern is useful for notifying an object or a group of objects when 
the state of a given object changes. This type of traditional Observer applies the 
publish-subscribe principle, allowing us to react to  some object change events. 
It provides a nice solution for many cases, but in a situation where we have to deal 
with many events, some of them depending on each other, the traditional way could lead 
to complicated, difficult-to-maintain code. That is where another paradigm called 
reactive programming gives us an interesting option. In simple terms, the
concept of reactive programming is to react to many events, streams of events, while
keeping our code clean.


An Observable is the core type in ReactiveX. It serially pushes items, known as
emissions, through a series of operators until it finally arrives at an Observer, where they
are consumed.


Push-based (rather than pull-based) iteration opens up powerful new possibilities to
express code and concurrency much more quickly. Because an Observable treats events as
data and data as events, composing the two together becomes trivial.

