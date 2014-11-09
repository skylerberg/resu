======
Design
======

Trade-offs
==========

For the sake of simplicity, Resu usually passes an entire resume and all associated metadata from function to function. This makes it easier to make Transforms follow a uniform interface because they all just take `data` as an argument. However, this desicion costs in terms of scalability because if the amount of data where too large, operations that look at the entire data set could become too costly. Further, this descision makes it less clear what parts of the data different functions actually operate on.

