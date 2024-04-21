# The Retry pattern


Retrying is an approach that is more and more needed in the context of microservices and
cloud-based infrastructure where components collaborate with each other, but are not
developed, deployed, and operated by the same teams and parties.

In its daily operation, parts of a cloud-native application may experience what is called
transient faults or failures, meaning some mini-issues that can look like bugs, but are not due
to your application itself but to some constraints outside of your control such as the
networking or the external server/service performance. As a result, your application may
dysfunction (at least that could be the perception of your users) or even hang at some
places. The answer to the risk of such failures is to put in place some retry logic, so that we
pass through the issue, by calling the service again, maybe immediately or after some wait
time (such as a few seconds).


This pattern is recommended to alleviate the impact of identified transient failures while
communicating with an external component or service, due to network failure or server
overload.

Note that the retrying approach is not recommended for handling failures such as internal
exceptions caused by errors in the application logic itself.

Also, we have to think about and analyze the way the external service responds. If the
application experiences frequent busy faults, it's often a sign that the service being accessed
has a scaling issue that should be addressed.