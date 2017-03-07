# Database Read-Phenomena Examples
Examples written in Python using threading to demonstrate different read phenomenons that occur in a database system.


##### Fuzzy Read
```
Fuzzy reads occur when a database transaction re-reads data it has already read,
and then finds that another committed transaction has modified or deleted the same data.
```

The example tries to simulate a situation where in the data is updated by one thread (A thread being considered as a database in this case), and another thread tries to read the value after the transaction is committed. But now let's assume, the old transaction is to be rolled back due to some error and gets committed. So when the second thread re-reads the data from the first thread, the data is (supposedly) updated. This leads to an error known as fuzzy read, which is also known as non-repeatable read. Locks can be used to avoid such errors.
