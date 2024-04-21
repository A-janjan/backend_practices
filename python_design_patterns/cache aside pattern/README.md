# The Cache-Aside pattern


In situations where data is more frequently read than updated, applications use a cache to
optimize repeated access to information stored in a database or data store. In some systems,
that type of caching mechanism is built-in and works automatically. When this is not the
case, we have to implement it in the application ourselves, using a caching strategy that is
suitable for the particular use case.


One such strategy is called Cache-Aside:

+ Load data on demand into a cache from a data store, as an attempt to improve performance,
while maintaining consistency between data held in the cache and the data in the
underlying data store.


The Cache-Aside pattern is useful for data that doesn't change often, and for data storage
that doesn't depend on the consistency of a set of entries in the storage (multiple keys). For
example, it might work for certain kinds of document stores, where keys are never
updated, and occasionally documents are deleted but there is no strong requirement to
continue to serve them for some time (until the cache is refreshed).


Also, according to the documentation, we can find (from Microsoft), this pattern might not
be suitable in the cases where the cached data set is static, or for caching session state
information in a web application hosted in a web farm.