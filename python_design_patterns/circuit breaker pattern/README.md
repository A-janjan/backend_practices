# The Circuit Breaker pattern


when a failure due to the communication with an external component is likely to be long-
lasting, using a retry mechanism can affect the responsiveness of the application. We might
be wasting time and resources trying to repeat a request that's likely to fail. This is where
another pattern can be useful, the Circuit Breaker.


With circuit breaker, you wrap a fragile function call (or an integration point with an
external service) in a special (circuit breaker) object, which monitors for failures. Once the
failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit
breaker return with an error, without the protected call being made at all.