# Hash Tables
# key vocab: associative arrays, hash functions, key/value pairs, collision, and chaining.
# A hash table consists of an array of pockets or buckets where each stores a key/value pair. In
# order to locate the pocket where a key/value should be stored the key is passed through a hashing
# function. This function returns an integer which is used as the pair's index in the array of
# buckets. When we want to retrieve a key/value pair we supply the key to the same hashing
# function, receive its index, and use the index to find it in the array.
# Associative arrays can be implemented with many underlying data structures and
# refers to an array with strings as an index rather than storing element values in a strict linear index
# order. This stores them in combination with key values. Multiple indices are used as values in a multidemensional
# array, which contains one or more arrays. Non-performant; no indexing, additions, removals or calls.
# Hash tables can be used to store, retrieve, delete based on their unique key. The most valuable aspect
# over other data structures is its speed to perform insertion, deletion and search operations. (constant time)