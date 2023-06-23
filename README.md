# Bridge (Structural)

Decouple an abstraction from its implementation so that the two can vary independently

Bridge is useful when:
- You want to avoid a permanent binding between an abstraction and its implementation. (when implementation must be selected or switched at run-time)
- Both the abstractions and their implementations should be extensible by subclassing.
- Changes in the implementation of an abstraction have no impact on clinets  (their code should not have to be recompiled)
- You want to share an implementation among multiple objects and this should be hidden from the client.

**Benefits:**

- Decoupling interface and implementation. An implementation is not bound permanently to an interface. This also eliminates compile-time dependencies on the implementation.
- Improved extensibility. Can extend the abstraction and implementor hierarchies independently.
- Hiding implementation details from clients.
