timeshift
===

A micro time zone conversion implementation for administrative purposes.

Motivation:
In cloud computing environments it is common to spin up (virtual) machine 
instances all the time. In these cases, you do not want to incur the cost 
of accessing a database, whatever the implementation, just to convert 
between time zones. 
The more time zones needed to support, the more overhead you have in one
way or another. Very frequently, you really just need to convert between 
UTC and one other time zone. 
This library addresses that problem.

If you need to support many, or all, time zones, there are better implementations.
See pytz for example.
